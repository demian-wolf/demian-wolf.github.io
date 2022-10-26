class TabManager {
    constructor (tabs) {
        this.tabs = [];
        document.addEventListener("DOMContentLoaded", () => {
            Array.prototype.forEach.call(
                tabs,
                tabElement => tabManager.tabs.push(new Tab(tabElement))
            );
            this.tabs[0].goto();
        });
    }

    reset() {
        for (const tab of this.tabs) tab._hide();
    }
}

class Tab {
    constructor(element) {
        this.element = element;

        this.buttonElement = document.createElement("a");
        this.buttonElement.classList.add("button", "portfolio__tab_button");
        this.buttonElement.addEventListener("click", () => this.goto());

        document.querySelector(
            "#portfolio__tabs_buttons"
        ).appendChild(this.buttonElement);
    }

    _show() {
        this.element.style.display = "block";
        this.buttonElement.classList.add("portfolio__tab_button_active");
    }

    _hide() {
        this.element.style.display = "none";
        this.buttonElement.classList.remove("portfolio__tab_button_active");
    }

    goto() {
        tabManager.reset();
        this._show();
    }
}

tabManager = new TabManager(
    document.getElementsByClassName("portfolio__tab")
);