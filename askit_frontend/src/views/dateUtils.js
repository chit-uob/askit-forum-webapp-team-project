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

export { formatPubDate };
export { formatDay };
export { formatMonthYear };