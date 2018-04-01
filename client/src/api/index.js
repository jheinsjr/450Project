import axios from 'axios'

//Trying to define functions for our api calls
//IDK if this is a good way to do it

const config = {
  address: 'http://127.0.0.1:8080',
  debug: true
}

function apiCall (api, method) {
  const url = `${config.address}/api/${api}`
  return async function (data, successCallback, failedCallback) {
    try {
      const response = await axios.request({
        url: url,
        method: method,
        data: data
      })

      if (response.data.status === 'success') {
        successCallback(response.data)
      } else {
        failedCallback(response.data.reason)
      }
    } catch (e) {
      failedCallback(e)
    }
  }
}

export default {
  login: apiCall('login', 'POST'),
  logout: apiCall('logout', 'GET'),
  get_tasks: apiCall('task-list', 'GET')
}
