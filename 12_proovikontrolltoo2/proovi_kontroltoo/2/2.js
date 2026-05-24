class Jook{
    nimetus; erikaal; omahind;
    constructor(nimetus, erikaal, omahind){
        this.nimetus = nimetus;
        this.erikaal = erikaal;
        this.omahind = omahind;
    }
}

class Joogipudel{
    maht; pudelityyp; mass; tara_maksumus; jook;
    constructor(maht, pudelityyp, mass, tara_maksumus, jook = null){
        this.maht = maht;
        this.pudelityyp = pudelityyp;
        this.mass = mass;
        this.tara_maksumus = tara_maksumus;
        this.jook = jook;
    }
    get mass_kokku(){
        if(this.jook === null){
            return this.mass;
        }
        return this.mass + this.jook.erikaal * this.maht;
    }
    get omahind_kokku(){
        if(this.jook === null){
            return this.tara_maksumus;
        }
        return this.tara_maksumus + this.jook.omahind * this.maht;
    }
}

class Joogivaat{
    ruumala; kogus;
    constructor(ruumala, kogus){
        this.ruumala = ruumala;
        this.kogus = kogus;
    }
    fillpudel(pudel){
        if(this.kogus >= pudel.maht){
            this.kogus -= pudel.maht;
        }
    }
    fillpudelid(pudelid){
        for(let i = 0; i < pudelid.length; i++){
            if(this.kogus >= pudelid[i].maht){
                this.kogus -= pudelid[i].maht;
            }
        }
    }
}


class JoogipudeliteKast{
    kastityyp; kastihind; kastimass; pesade_arv;
    constructor(kastityyp, kastihind, kastimass, pesade_arv){
        this.kastityyp = kastityyp;
        this.kastihind = kastihind;
        this.kastimass = kastimass;
        this.pesade_arv = pesade_arv;
    }
    fillkast(pudelid){
        return pudelid.slice(0, this.pesade_arv);
    }
    pudelite_mass(pudelid){
        let sum = 0;
        for(let i=0; i<pudelid.length; i++){
            sum += pudelid[i].mass_kokku;
        }
        return sum;
    }
    pudelite_omahind(pudelid){
        let sum = 0;
        for(let i=0; i<pudelid.length; i++){
            sum += pudelid[i].omahind_kokku;
        }
        return sum;
    }
}


const jook1 = new Jook("Coca-Cola", 1.2, 0.5);
const jook2 = new Jook("Fanta", 1.1, 0.4);
const jook3 = new Jook("Sprite", 1.0, 0.3);

const pudel1 = new Joogipudel(0.5, "Plastik", 0.1, 0.2, jook1);
const pudel2 = new Joogipudel(1.0, "Plastik", 0.2, 0.3, jook2);
const pudel3 = new Joogipudel(1.5, "Plastik", 0.3, 0.4, jook3);

const kast1 = new JoogipudeliteKast("Plastik", 5.0, 1.0, 2);
const kastis_pudelid = kast1.fillkast([pudel1, pudel2, pudel3]);
console.log("Kastis pudelite mass kokku:", kast1.pudelite_mass(kastis_pudelid) + kast1.kastimass);
console.log("Kastis pudelite omahind kokku:", kast1.pudelite_omahind(kastis_pudelid) + kast1.kastihind);