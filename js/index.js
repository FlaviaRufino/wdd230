let today1 = new Date()
let year = today1.getFullYear();
let fulldate = `${year}`;
document.querySelector("#year").textContent = fulldate;

let lastmod = new Date(document.lastModified)
document.querySelector("#updated").textContent = lastmod;


let todaystr = "";
switch (today1.getDay()) {
    case 0:
        todaystr = "Sunday";
        break;
    case 1:
        todaystr = "Monday";
        break;
    case 2:
        todaystr = "Tuesday";
        break;
    case 3:
        todaystr = "Wednesday";
        break;
    case 4:
        todaystr = "Thursday";
        break;
    case 5:
        todaystr = "Friday";
        break;
    case 6:
        todaystr = "Saturday";
        break;
}
let month = "";

switch (today1.getMonth()) {
    case 0:
        month = "January";
        break;
    case 1:
        month = "February";
        break;
    case 2:
        month = "March";
        break;
    case 3:
        month = "April";
        break;
    case 4:
        month = "May";
        break;
    case 5:
        month = "June";
        break;
    case 6:
        month = "July";
        break;
    case 7:
        month = "August";
        break;
    case 8:
        month = "September";
        break;
    case 9:
        month = "October";
        break;
    case 10:
        month = "November";
        break;
    case 11:
        month = "December";
        break;
}

let todayconcat = todaystr + ", " + today1.getDate() + " " + month + " " + year;
document.querySelector("#today").textContent = todayconcat;
