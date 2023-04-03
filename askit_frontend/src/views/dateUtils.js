import dayjs from "dayjs";

function formatPubDate(pubDate) {
    return dayjs(pubDate).format("DD/MM/YYYY HH:mm");
}

function formatDate(pubDate) {
    return dayjs(pubDate).format("DD/MM/YY");
}

function formatDay(pubDate) {
    return dayjs(pubDate).format("DD");
}

function formatMonthYear(pubDate) {
    return dayjs(pubDate).format("MMMYY");
}

function withinTime(pubDate, timeFrame) {
    //console.log( dayjs(pubDate).toString())
    //console.log(dayjs().subtract(timeFrame,'day').toString())
    if (dayjs(pubDate).isAfter(dayjs().subtract(timeFrame,'day'))){
        console.log( dayjs(pubDate).toString() + " is after " + dayjs(pubDate).subtract(timeFrame,'day').toString())
        return true
    }
    else{
        return false
    }
    //return dayjs(pubDate).isAfter(dayjs(dayjs.locale()).subtract(timeFrame,'day'))
}

export { formatPubDate };
export { formatDate };

export { formatDay };
export { formatMonthYear };
export { withinTime }