const mobileMenuBtn = document.querySelector('#burgerBtn')
const mobileMenu = document.querySelector('#mobileMenu')
const closeBtn = document.querySelector('#quitMenu')

mobileMenuBtn.addEventListener('click', () => {
  mobileMenu.style.right = '0'
})

closeBtn.addEventListener('click', () => {
  mobileMenu.style.right = '-225px'
})
