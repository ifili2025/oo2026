//Esimene punkt
function keskmine(arv1, arv2, arv3) {
    return (arv1 + arv2 + arv3) / 3;
}
function libisevKeskmine(arvud) {
    let keskmised = [];
    for (let i = 2; i < arvud.length; i++) {
        let keskmineArv = keskmine(arvud[i-2], arvud[i-1], arvud[i]);
        keskmised.push(keskmineArv);
    }
    return keskmised;
}

console.log(keskmine(5, 10, 15));

console.log(libisevKeskmine([5, 10, 15, 35]));

//Teine punkt
class LibisevKeskmine {
    constructor() {
        this.arvud = [];
        this.keskmised = [];
    }
    lisaArv(arv) {
        this.arvud.push(arv);
        let n = this.arvud.length;
        if (n >= 3){
            let keskmine = (this.arvud[n-3] + this.arvud[n-2] + this.arvud[n-1]) / 3;
            this.keskmised.push(keskmine);
        }
        //console.log(this.keskmised);
    }
    leiaKeskmised() {
        return this.keskmised
    }
}

let lk = new LibisevKeskmine();
lk.lisaArv(5);
lk.lisaArv(10);
lk.lisaArv(15);
lk.lisaArv(35);

lk.leiaKeskmised();
console.log(lk.keskmised);
