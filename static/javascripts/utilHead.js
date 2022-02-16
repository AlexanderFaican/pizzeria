function getDateString(date, format){
    var months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    var date = new Date(date);

    var hour = date.getHours();
    hour = (hour < 10 ? "0" : "") + hour;

    var min = date.getMinutes();
    min = (min < 10 ? "0" : "") + min;

    var sec = date.getSeconds();
    sec = (sec < 10 ? "0" : "") + sec;

    var year = date.getFullYear();

    var month = date.getMonth() + 1;
    month = (month < 10 ? "0" : "") + month;
    var add = (hour == "19" && min == "00" && sec == "00")? 1 : 0;
    var day = date.getDate() + add;
    day = (day < 10 ? "0" : "") + day;
    var out = "";
    switch(format){
        case "DD/MM":
            out = day + "/" + month;
            break;
        case "DD MM":
            out = day + " " + months[month-1];
            break;
        case "DD MM YYYY":
            out = day + " de " + months[month-1] + " del " + year;
            break;
        case "DD-MM-YYYY":
            out = day + "-" + month + "-" + year;
            break;
        case "DD/MM/YYYY":
            out = day + "/" + month + "/" + year;
            break;
        case "DD/MM/YYYY HH:MM":
            out = day + "/" + month + "/" + year + " " + hour + ":" + min;
            break;
        case "DD MM YYYY HH:MM":
            out = day + " de " + months[month-1] + " del " + year + " a las " + hour + ":" + min;
            break;
        case "DD MM YYYY HH MM":
            out = day + " de " + months[month-1] + " del " + year + " a las " + hour + " horas " + min + " minutos";
            break;
        case "HH:MM":
            out = hour + ":" + min;
            break;
        default:
            out = "Fecha invalida";
    }
    return out;
}

function round(num, decimales = 2) {
    var signo = (num >= 0 ? 1 : -1);
    num = num * signo;
    if (decimales === 0) //con 0 decimales
        return signo * Math.round(num);
    // round(x * 10 ^ decimales)
    num = num.toString().split('e');
    num = Math.round(+(num[0] + 'e' + (num[1] ? (+num[1] + decimales) : decimales)));
    // x * 10 ^ (-decimales)
    num = num.toString().split('e');
    return signo * (num[0] + 'e' + (num[1] ? (+num[1] - decimales) : -decimales));
}
