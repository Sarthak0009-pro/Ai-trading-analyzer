async function uploadChart() {

const file = document.getElementById("chartUpload").files[0]

const formData = new FormData()
formData.append("chart", file)

const response = await fetch("http://localhost:8000/analyze", {
method: "POST",
body: formData
})

const data = await response.json()

document.getElementById("result").innerText =
"Entry: " + data.entry +
" SL: " + data.sl +
" TP: " + data.tp

}
