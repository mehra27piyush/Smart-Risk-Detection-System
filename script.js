async function checkRisk() {
    const age = document.getElementById("age").value;
    const hr = document.getElementById("heartRate").value;
    const ox = document.getElementById("oxygen").value;

    const res = await fetch(`http://127.0.0.1:8000/predict?age=${age}&hr=${hr}&ox=${ox}`);
    const data = await res.json();

    document.getElementById("result").innerText = "Risk Level: " + data.risk;
}