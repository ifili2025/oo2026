class Veekeedukann {
    constructor() {
        this.veemahutavus = 2000; 
        this.veekogus = 500;
        this.temperatuur = 20; 
        this.võimsus = 1200;
    }
    kasKuum() {
        return this.temperatuur >= 80;
    }
    kuumuta(sekundid) {
    let energia = this.võimsus * sekundid;
    let temperatuuritous = energia / (this.veekogus * 4.19);
    this.temperatuur += temperatuuritous;
}
    lisaVett(milliliitrid, kraadid) {
        let uusKogus = this.veekogus + milliliitrid;
        if (uusKogus > this.veemahutavus) {
            console.log("ei saa nii palju lisada");
            return;
        }
        let uusTemperatuur = (this.temperatuur * this.veekogus + kraadid * milliliitrid) / uusKogus;
        this.veekogus = uusKogus;
        this.temperatuur = uusTemperatuur;
    }
}

let kann = new Veekeedukann();
console.log(kann.kasKuum());
//kann.kuumuta(10);
console.log(kann.temperatuur);
kann.lisaVett(500, 10);
console.log(kann.temperatuur);
kann.lisaVett(2000, 10);
