import axios from 'axios'
// 通过export导出多个实例 export default只能导出一个实例
axios.defaults.baseURL = 'http://127.0.0.1:8000';
export function loginRequest(config){
    //创建axios实例
    const loginRequest = axios.create({
        url: '/api/login/confirmAuth/',
        timeout: 10000,
        method: 'post',
        headers:{
            'Content-Type': 'application/json',
        }
    });
    // 发送真正的网络请求
    return loginRequest(config)
    //如果有一天，此axios无法使用，在loginRequest内重构新代码，return Promise(config)即可
}

export function wordRequest(config){
    const wordRequest = axios.create({
        url: '/api/homepage/words/',
        timeout: 10000,
        headers:{
            'Content-Type': 'application/json',
        }
    });
    return wordRequest(config)
}

export function photoRequest(config){
    const photoRequest = axios.create({
        url: '/api/homepage/photos/',
        timeout: 10000,
        headers:{
            'Content-Type': 'application/json',
        }
    });
    return photoRequest(config)
}
