const totalPortfolioTabs = 3;

function showPortfolioTab(tabId) {
    const tab = document.getElementById(`portfolio__tab${tabId}`);
    const tabButton = document.getElementById(`portfolio__tab${tabId}_button`);

    tab.style.display = "block";
    tabButton.classList.add("portfolio__tab_button_active");
}

function hidePortfolioTab(tabId) {
    const tab = document.getElementById(`portfolio__tab${tabId}`);
    const tabButton = document.getElementById(`portfolio__tab${tabId}_button`);

    tab.style.display = "none";
    tabButton.classList.remove("portfolio__tab_button_active");
}

function gotoPortfolioTab(destTabId) {
    for (let tabId = 1; tabId <= totalPortfolioTabs; tabId++) {
        tabId === destTabId ? showPortfolioTab(tabId) : hidePortfolioTab(tabId);
    }
}

function resetPortfolioTabs() {
    for (let tabId = 1; tabId <= totalPortfolioTabs; tabId++) {
        hidePortfolioTab(tabId);
    }
}

document.addEventListener("DOMContentLoaded", () => gotoPortfolioTab(1));
