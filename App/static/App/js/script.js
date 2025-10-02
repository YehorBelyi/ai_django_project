document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("chat-form");
    const input = document.getElementById("message");
    const chatBox = document.getElementById("chat-box");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const message = input.value.trim();
        if (!message) return;

        addMessage("user", message);
        input.value = "";

        try {
            const response = await fetch("/app/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken()
                },
                body: JSON.stringify({ message })
            });

            const data = await response.json();
            addMessage("ai", data.ai_message);
        } catch (err) {
            addMessage("ai", "⚠️ Server error!");
        }
    });

    function addMessage(sender, text) {
        const msgDiv = document.createElement("div");
        msgDiv.classList.add("p-3", "rounded-lg", "max-w-xl");

        if (sender === "user") {
            msgDiv.classList.add("bg-blue-100", "self-end", "ml-auto");
        } else {
            msgDiv.classList.add("bg-gray-200", "self-start", "mr-auto");
        }

        msgDiv.textContent = text;
        chatBox.appendChild(msgDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function getCSRFToken() {
        let cookieValue = null;
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith("csrftoken=")) {
                cookieValue = cookie.substring("csrftoken=".length);
                break;
            }
        }
        return cookieValue;
    }
});

const textarea = document.getElementById("message");

textarea.addEventListener("input", autoResize, false);

function autoResize() {
    this.style.height = "auto";
    this.style.height = this.scrollHeight + "px";
}
