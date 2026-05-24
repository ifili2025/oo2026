class Hulknurk{
    kesk_x; kes_y;
    tipu_kaugus;
    tipude_arv;
    constructor(kesk_x, kes_y, tipu_kaugus, tipude_arv){
        this.kesk_x = kesk_x;
        this.kesk_y = kes_y;
        this.tipu_kaugus = tipu_kaugus;
        this.tipude_arv = tipude_arv;
    }
    get area(){
        return 0.5 * this.tipude_arv * this.tipu_kaugus ** 2 * Math.sin(2 * Math.PI / this.tipude_arv);
    }
    get tipud(){
        let tipud = [];
        for(let i = 0; i < this.tipude_arv; i++){
            tipud.push([
            this.kesk_x + this.tipu_kaugus * Math.cos(2 * Math.PI * i / this.tipude_arv),
            this.kesk_y + this.tipu_kaugus * Math.sin(2 * Math.PI * i / this.tipude_arv)
            ]);
        }
        return tipud;
    }
    draw(g){
        g.clearRect(0,0, canvas1.width, canvas1.height)
        g.beginPath();
        g.moveTo(this.tipud[0][0], this.tipud[0][1]);
        for(let i = 1; i < this.tipude_arv; i++){
            g.lineTo(this.tipud[i][0], this.tipud[i][1]);
        }
        g.lineTo(this.tipud[0][0], this.tipud[0][1]);
        g.stroke();
    }
}

// c = new Hulknurk(0, 0, 5, 3);
// console.log(c.area);
// console.log(c.tipud);