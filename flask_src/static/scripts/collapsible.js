const totalCollapsibles = 3;

function _getCollapsible(collapsibleId) {
    return document.getElementById(`collapsible${collapsibleId}`);
}

function _getCollapsibleContent(collapsibleId) {
    return _getCollapsible(collapsibleId).querySelector(".collapsible__content");
}

function _getCollapsibleArrow(collapsibleId) {
    return _getCollapsible(collapsibleId).querySelector(".collapsible__arrow")
}

function collapsibleSetState(collapsibleId, destState) {
    _getCollapsibleContent(collapsibleId).style.display = destState ? "block" : "none";
    _getCollapsibleArrow(collapsibleId).innerHTML = destState ? "\u25B2" : "\u25BC";
}

function collapsibleToggle(collapsibleId) {
    const newState = _getCollapsibleContent(collapsibleId).style.display === "none";
    collapsibleSetState(collapsibleId, newState);
}

document.addEventListener("DOMContentLoaded", () => {
    for (let collapsibleId = 1; collapsibleId <= totalCollapsibles; collapsibleId++) {
        collapsibleSetState(collapsibleId, false);
    }
});
