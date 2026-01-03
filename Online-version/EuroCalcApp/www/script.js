    // Универсална функция за парсване на числа
    function parseAmount(value) {
        value = value.replace(',', '.').trim();
        let num = parseFloat(value);
        return isNaN(num) ? 0.0 : num;
    }

    // Основен калкулатор: Ресто в евро
    const input_due = document.getElementById('input_due');
    const input_paid_lev = document.getElementById('input_paid_lev');
    const input_paid_eur = document.getElementById('input_paid_eur');
    const btn_calc = document.getElementById('btn_calc');
    const label_result = document.getElementById('label_result');

    btn_calc.addEventListener('click', () => {
        const due = parseAmount(input_due.value);
        const paid_lev = parseAmount(input_paid_lev.value);
        const paid_eur = parseAmount(input_paid_eur.value);
        const rate = 1.95583;
        const total_paid_eur = paid_eur + (paid_lev / rate);
        const change_eur = total_paid_eur - due;
        label_result.innerText = `Ресто в ЕВРО: ${change_eur.toFixed(2)}`;
    });

    // Евро → Лева
    const btnEurToLev = document.getElementById('btn_eur_to_lev');
    const inputEurToLev = document.getElementById('input_eur_to_lev');
    const resultEurToLev = document.getElementById('result_eur_to_lev');

    btnEurToLev.addEventListener('click', () => {
        const eur = parseAmount(inputEurToLev.value);
        const lev = eur * 1.95583;
        resultEurToLev.innerText = `${lev.toFixed(2)} лева`;
    });

    // Лева → Евро
    const btnLevToEur = document.getElementById('btn_lev_to_eur');
    const inputLevToEur = document.getElementById('input_lev_to_eur');
    const resultLevToEur = document.getElementById('result_lev_to_eur');

    btnLevToEur.addEventListener('click', () => {
        const lev = parseAmount(inputLevToEur.value);
        const eur = lev / 1.95583;
        resultLevToEur.innerText = `${eur.toFixed(2)} евро`;
    });

    function clearOnFocus(element) {
    element.addEventListener('focus', function() {
        if (this.value === '' || this.value === '0.00') {
            this.value = '';
        }
    });
    element.addEventListener('blur', function() {
        if (this.value === '') {
            this.value = '0.00';
        }
    });
}

    clearOnFocus(document.getElementById('input_due'));
    clearOnFocus(document.getElementById('input_paid_lev'));
    clearOnFocus(document.getElementById('input_paid_eur'));
    clearOnFocus(document.getElementById('input_eur_to_lev'));
    clearOnFocus(document.getElementById('input_lev_to_eur'));
