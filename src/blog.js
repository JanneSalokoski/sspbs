function get_preferred_colorscheme() {
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.getElementById("body").classList.add("dark")
  }
}

function toggle_colorscheme() {
  document.getElementById("body").classList.toggle("dark")
}

function init() {
  get_preferred_colorscheme()
}

document.addEventListener("DOMContentLoaded", () => {
  init()
})
