
// * Koosta klass Joogivaat, millel on ruumala ning sees oleva Joogi kogus liitrites. 
// Koosta käsk etteantud Joogipudeli täitmiseks (juhul kui Jooki jagub). 
// Koosta käsklus kogu Joogivaaditäie Joogi villimiseks Joogipudelitesse, tühjad pudelid tuleb käsule ette anda. 
// Koosta töö kontrolliks automaattestid.
// * Koosta Joogipudelite Kasti jaoks klass. Väljadeks kastityyp, kastihind, kastimass ning pesade arv (mitu pudelit mahub). 
// Loo käsklused kasti ja sinna kuuluvate pudelite ühise massi ja omahinna arvutamiseks. 
// Loo käsklus Joogivaadist Kasti sisse pudelite villimiseks. Koosta automaattestid.
class Jook{
    nimetus; omahind; erikaal;
    constructor(nimetus, omahind, erikaal){
        this.nimetus = nimetus;
        this.omahind = omahind;
        this.erikaal = erikaal;
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
        if(this.jook===null){
            return this.mass;
        }
        return this.mass + this.jook.erikaal * this.maht;
    }
    get omahind_kokku(){
        if(this.jook===null){
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
        this.kastimass = kastimass
        this.pesade_arv = pesade_arv;
    }
    pudelite_mass(pudelid){
        let mass = 0;
        for(let i = 0; i < pudelid.length; i++){
            mass += pudelid[i].mass_kokku;
        }
        return this.kastimass + mass;
    }
    pudelite_omahind(pudelid){
        let omahind = 0;
        for(let i = 0; i < pudelid.length; i++){
            omahind += pudelid[i].omahind_kokku;
        }
        return this.kastihind + omahind;
    }
    fillkast(pudelid){
        let pudelid_kastis = [];
        for(let i = 0; i < pudelid.length && i < this.pesade_arv; i++){
            pudelid_kastis.push(pudelid[i]);
            this.kastimass += pudelid[i].mass;
            this.kastihind += pudelid[i].tara_maksumus;
            if(pudelid[i].jook!=null){
                this.kastihind += pudelid[i].jook.omahind * pudelid[i].maht;
                this.kastimass += pudelid[i].jook.erikaal * pudelid[i].maht;
            }
        }
        return pudelid_kastis;
    }
}

const jook1 = new Jook("Vesi", 0.5, 1);
const puudel1 = new Joogipudel(1, "Plastik", 0.2, 0.1, null);
const puudel2 = new Joogipudel(1, "Plastik", 0.2, 0.1, jook1); 
// console.log(puudel1.mass_kokku);
// console.log(puudel1.omahind_kokku);
// console.log(puudel2.mass_kokku);
// console.log(puudel2.omahind_kokku);
const vaat1 = new Joogivaat(1, 1);
vaat1.fillpudel(puudel1);
// console.log("Jäänud liitrid: " +vaat1.kogus);
const vaat2 = new Joogivaat(3, 3);
vaat2.fillpudelid([puudel1, puudel1, puudel1]);
// console.log("Jäänud liitrid: " +vaat2.kogus);



const puudel3 = new Joogipudel(1, "Plastik", 0.2, 0.1, jook1); 
const puudel4 = new Joogipudel(1, "Plastik", 0.2, 0.1, jook1); 
const kast1 = new JoogipudeliteKast("Plastik", 0.5, 0.3, 2);
console.log("Kasti mass kokku: " + kast1.pudelite_mass([puudel3, puudel4]));
console.log("Pudelite omahind kokku: " + kast1.pudelite_omahind([puudel3, puudel4]));
console.log("Pudelite mass kastis: " + kast1.pudelite_mass(kast1.fillkast([puudel3, puudel4, puudel1])));
console.log("Pudelite omahind kastis: " + kast1.pudelite_omahind(kast1.fillkast([puudel3, puudel4, puudel1])));

