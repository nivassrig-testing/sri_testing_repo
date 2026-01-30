async function sendMessage() {
    const input = document.getElementById('userInput');
    const btn = document.getElementById('sendBtn');
    const container = document.getElementById('chatContainer');
    
    const text = input.value.trim();
    if (!text) return;

    // Add User Message
    addMessage(text, 'user');
    input.value = '';
    input.disabled = true;
    btn.disabled = true;
    
    // Show loading
    const loadingId = addLoading();

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ input: text })
        });
        
        const data = await response.json();
        removeMessage(loadingId);
        
        if (data.error) {
            addMessage(`Error: ${data.error}`, 'system');
        } else {
            renderTestCases(data.test_cases, data.summary);
        }
        
    } catch (e) {
        removeMessage(loadingId);
        addMessage(`Network Error: ${e}`, 'system');
    }

    input.disabled = false;
    btn.disabled = false;
    input.focus();
}

function addMessage(text, type) {
    const container = document.getElementById('chatContainer');
    const msg = document.createElement('div');
    msg.className = `message ${type}`;
    msg.innerHTML = `
        <div class="avatar">${type === 'user' ? 'U' : 'AI'}</div>
        <div class="bubble"><p>${text}</p></div>
    `;
    container.appendChild(msg);
    container.scrollTop = container.scrollHeight;
}

function addLoading() {
    const container = document.getElementById('chatContainer');
    const id = 'loading-' + Date.now();
    const msg = document.createElement('div');
    msg.id = id;
    msg.className = 'message system';
    msg.innerHTML = `
        <div class="avatar">AI</div>
        <div class="bubble"><p>Thinking...</p></div>
    `;
    container.appendChild(msg);
    container.scrollTop = container.scrollHeight;
    return id;
}

function removeMessage(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
}

function renderTestCases(testCases, summary) {
    const container = document.getElementById('chatContainer');
    const msg = document.createElement('div');
    msg.className = 'message system';
    
    let html = `<div class="avatar">AI</div><div class="bubble">`;
    if (summary) html += `<p><strong>Summary:</strong> ${summary}</p>`;
    
    if (testCases && testCases.length) {
        testCases.forEach(tc => {
            html += `
            <div class="test-case-card">
                <div class="tc-header">
                    <span class="tc-id">${tc.id}</span>
                    <span class="tc-title">${tc.title || tc.description.substring(0, 30)+'...'}</span>
                </div>
                <div class="tc-body">
                    <p><strong>Desc:</strong> ${tc.description}</p>
                    <p><strong>Expected:</strong> ${tc.expected_result}</p>
                    <div class="tc-steps">
                        <strong>Steps:</strong>
                        <ol>
                            ${tc.steps.map(s => `<li>${s.replace(/^\d+\.\s*/, '')}</li>`).join('')}
                        </ol>
                    </div>
                </div>
            </div>
            `;
        });
    }
    
    html += `</div>`;
    msg.innerHTML = html;
    container.appendChild(msg);
    container.scrollTop = container.scrollHeight;
}

// Enter key support
document.getElementById('userInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});
