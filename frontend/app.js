function sendData() {
  const name = document.getElementById("name").value;
  const message = document.getElementById("message").value;

  fetch("/submit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      name: name,
      message: message
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerText = data.status;
  });
}

