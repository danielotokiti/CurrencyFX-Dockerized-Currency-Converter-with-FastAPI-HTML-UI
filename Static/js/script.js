document.getElementById('convert-btn').addEventListener('click', async () => {
    const amount = document.getElementById('amount').value;
    const from = document.getElementById('from-currency').value;
    const to = document.getElementById('to-currency').value;
    const resultDiv = document.getElementById('result');
    
    resultDiv.innerHTML = "Converting...";
    
    try {
        const response = await fetch(
            `/convert?from_currency=${from}&to_currency=${to}&amount=${amount}`
        );
        const data = await response.json();
        
        if (data.success) {
            resultDiv.innerHTML = `
                <strong>${amount} ${from} = ${data.result} ${to}</strong><br>
                <small>Rate: 1 ${from} = ${data.rate} ${to}</small>
            `;
        } else {
            resultDiv.innerHTML = `<span class="error">Error: ${data.message}</span>`;
        }
    } catch (error) {
        resultDiv.innerHTML = `<span class="error">Connection error</span>`;
    }
});