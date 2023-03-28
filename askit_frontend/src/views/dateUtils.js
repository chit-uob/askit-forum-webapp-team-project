import dayjs from "dayjs";

function formatPubDate(pubDate) {
    return dayjs(pubDate).format("DD/MM/YYYY HH:mm");
}

function formatDay(pubDate) {
    return dayjs(pubDate).format("DD");
}

function formatMonthYear(pubDate) {
    return dayjs(pubDate).format("MMMYY");
}

function withinTime(pubDate, timeFrame) {
    return dayjs(pubDate).isAfter((dayjs(dayjs.locale()).subtract(timeFrame,'day')))
}

export { formatPubDate };
export { formatDay };
export { formatMonthYear };
export { withinTime }