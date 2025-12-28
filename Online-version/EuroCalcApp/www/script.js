function parseAmount(value) {
    value = value.replace(',', '.').trim();
    let num = parseFloat(value);
    return isNaN(num) ? 0.0 : num;
}

function calculateChange() {
    let due = parseAmount(document.getElementById('due').value);
    let paid_lev = parseAmount(document.getElementById('paid_lev').value);
    let paid_eur = parseAmount(document.getElementById('paid_eur').value);

    let rate = 1.95583;
    let total_paid_eur = paid_eur + (paid_lev / rate);
    let change_eur = total_paid_eur - due;

    document.getElementById('due').value = due.toFixed(2);
    document.getElementById('paid_lev').value = paid_lev.toFixed(2);
    document.getElementById('paid_eur').value = paid_eur.toFixed(2);

    document.getElementById('result').textContent = `Ресто в ЕВРО: ${change_eur.toFixed(2)}`;
}