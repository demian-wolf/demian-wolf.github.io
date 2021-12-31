class Collapsible {
    constructor(element) {
        this.element = element;

        const titleElement = element.querySelector(".collapsible__title");
        this.title = titleElement.innerText;

        titleElement.innerHTML = `<a class="collapsible__toggle_link"><span class="collapsible__arrow"></span>${this.title}</a>`;

        this.toggleLinkElement = titleElement.querySelector(".collapsible__toggle_link");
        this.toggleLinkElement.setAttribute("href", "javascript:void(0);");
        this.toggleLinkElement.addEventListener("click", () => this.toggle());

        this.arrowElement = this.toggleLinkElement.querySelector(".collapsible__arrow");
        this.contentElement = element.querySelector(".collapsible__content");

        this.setState(false);
    }

    setState(destState) {
        this.contentElement.style.display = destState ? "block" : "none";
        this.arrowElement.innerHTML = destState ? "\u25B2" : "\u25BC";

        this.state = destState;
    }

    toggle() {this.setState(!this.state);}
}


document.addEventListener("DOMContentLoaded", () => {
    Array.prototype.forEach.call(
        document.getElementsByClassName("collapsible"),
        collapsibleElement => new Collapsible(collapsibleElement)
    );
});
