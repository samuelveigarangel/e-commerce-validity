class MobileNavbar{
    constructor(mobileMenu, menu, menuItem){
        this.mobileMenu = document.querySelector(mobileMenu);
        this.menu = document.querySelector(menu);
        this.menuItem = document.querySelectorAll(menuItem);
        this.activeClass = "active";
        
        this.handleClick = this.handleClick.bind(this);
    }
    
    animateLinks(){
    this.menuItem.forEach((link, index) =>{
        link.style.animation
        ? (link.style.animation = "")
        : (link.style.animation = `menuItemFade 0.5s ease forwards ${
            index / 7 + 0.3
          }s`);
    });
    }

    handleClick() {
        this.menu.classList.toggle(this.activeClass);
        this.mobileMenu.classList.toggle(this.activeClass);
        this.animateLinks();
    }


    addClickEvent() {
        this.mobileMenu.addEventListener("click", this.handleClick);
    }

    init(){
        if(this.mobileMenu){
            this.addClickEvent();
        }
        return this;
    }
}

const mobileNavbar = new MobileNavbar(
    ".mobile-menu",
    ".menu",
    ".menuItem",
);
mobileNavbar.init();

const searchBtn = document.querySelector(".search-icon");
const form = document.querySelector(".form-search")
const cancelBtn = document.querySelector(".cancel-icon")

cancelBtn.onclick = () =>{
    searchBtn.classList.remove("hide");
    cancelBtn.classList.remove("show");
    form.classList.remove("active");
}

searchBtn.onclick = () =>{
    form.classList.add("active")
    searchBtn.classList.add("hide");
    cancelBtn.classList.add("show");
}
