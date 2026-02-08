
document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const chatContainer = document.getElementById('chat-container');

    // Auto-resize textarea
    userInput.addEventListener('input', function () {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
        if (this.value === '') this.style.height = 'auto';
    });

    // Send on Enter (but Shift+Enter for newline)
    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    sendBtn.addEventListener('click', sendMessage);

    async function sendMessage() {
        const text = userInput.value.trim();
        if (!text) return;

        // Add User Message
        appendMessage(text, 'user-message');
        userInput.value = '';
        userInput.style.height = 'auto';

        // Add Loading Indicator
        const loadingId = appendLoading();

        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ user_input: text })
            });

            const data = await response.json();

            // Remove Loading
            removeMessage(loadingId);

            if (data.status === 'success') {
                appendMessage(data.html_content, 'ai-message', true);
            } else {
                appendMessage(`Error: ${data.message}`, 'ai-message error');
            }

        } catch (error) {
            removeMessage(loadingId);
            appendMessage(`System Error: ${error.message}`, 'ai-message error');
        }
    }

    function appendMessage(content, className, isHTML = false) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${className}`;

        if (isHTML) {
            msgDiv.innerHTML = content;
        } else {
            msgDiv.textContent = content;
        }

        chatContainer.appendChild(msgDiv);
        chatContainer.scrollTo({ top: chatContainer.scrollHeight, behavior: 'smooth' });
        return msgDiv;
    }

    function appendLoading() {
        const id = 'loading-' + Date.now();
        const msgDiv = document.createElement('div');
        msgDiv.id = id;
        msgDiv.className = 'message ai-message';
        msgDiv.textContent = 'Generating test cases...';
        chatContainer.appendChild(msgDiv);
        chatContainer.scrollTo({ top: chatContainer.scrollHeight, behavior: 'smooth' });
        return id;
    }

    function removeMessage(id) {
        const el = document.getElementById(id);
        if (el) el.remove();
    }
});
