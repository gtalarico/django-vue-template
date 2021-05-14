/**
 * Set localStorage
 */
export const setStore = (name, content) => {
  if (!name) return
  if (typeof content !== 'string') {
    content = JSON.stringify(content)
  }
  return window.localStorage.setItem(name, content)
}
/**
  * Get localStorage
*/
export const getStore = (name) => {
  if (!name) return
  return JSON.parse(window.localStorage.getItem(name))
}
/**
 * Clear localStorage
*/
export const removeItem = (name) => {
  if (!name) return
  return window.localStorage.removeItem(name)
}
/**
 * Validate Email address
 */
export const isValidEmail = (value) => {
  return value && !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,64}$/i.test(value) ? false : true
}
