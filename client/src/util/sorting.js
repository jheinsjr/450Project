export default {
  compareValues(keyGet, order = 'asc') {
    return function (a, b) {

      const aKey = keyGet(a)
      const bKey = keyGet(b)

      const varA = (typeof aKey === 'string') ?
        aKey.toUpperCase() : aKey
      const varB = (typeof bKey === 'string') ?
        bKey.toUpperCase() : bKey

      let comparison = 0
      if (varA > varB) {
        comparison = 1
      } else if (varA < varB) {
        comparison = -1
      }
      return (
        (order === 'desc') ? (comparison * -1) : comparison
      )
    }
  }
}
