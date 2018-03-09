import axios from 'axios'

const config = {
  address: 'http://127.0.0.1:8080',
  debug: true
}

function apiCall (api, method) {
  const url = `${config.address}/api/${api}`
  return function (data, successCallback, failedCallback) {
    axios.request({
      url: url,
      method: method,
      data: data
    }).then(response => {
      if (response.data.status === 'success') {
        successCallback(response.data)
      } else {
        failedCallback(response.data.reason)
      }
    })
      .catch(reason => {
        failedCallback(reason)
      })
  }
}

export default {
  login: apiCall('login', 'POST'),
  get_tasks: apiCall('get_tasks', 'GET')
}
