import dayjs from "dayjs";

function formatPubDate(pubDate) {
    return dayjs(pubDate).format("DD/MM/YYYY HH:mm");
}

export { formatPubDate };