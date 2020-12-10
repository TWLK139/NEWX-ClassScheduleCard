import Vue from 'vue'
import App from './App'

import cuCustom from './colorui/components/cu-custom.vue'
Vue.component('cu-custom', cuCustom)

Vue.config.productionTip = false
Vue.config.baseUrl = ["https://api.jw.huii.top/", "https://lesson.newxstudio.com/lesson/public/index.php/index/",
	"https://apply.newxstudio.com/", "https://www.newxstudio.com/index/", "https://www.newxstudio.com/admin/login/",
	"https://www.newxstudio.com/index/works/"
]
// Vue.config.baseUrl = ["http://jxglstu.hfut.edu.cn:7070/appservice/home/",
// 	"https://lesson.newxstudio.com/lesson/public/index.php/index/", "https://apply.newxstudio.com/",
// 	"https://www.newxstudio.com/index/", "https://www.newxstudio.com/admin/login/",
// 	"https://www.newxstudio.com/index/works/"
// ]
//Vue.config.baseUrl = ["http://127.0.0.1/", "https://lesson.newxstudio.com/lesson/public/index.php/index/", "https://apply.newxstudio.com/", "https://www.newxstudio.com/index/", "https://www.newxstudio.com/admin/login/", "https://www.newxstudio.com/index/works/"]
Vue.config.cookie = '';
Vue.config.shareImg = '';
Vue.config.version = 6;
// #ifdef APP-PLUS
Vue.config.platform = 0;
// #endif
// #ifdef MP-QQ
Vue.config.platform = 1;
// #endif
// #ifdef H5
Vue.config.platform = 2;
// #endif
Vue.config.student_id = '0000000000';
Vue.config.os_result = {};
Vue.config.applystatus = -1;
App.mpType = 'app';

Vue.prototype.simpleCheck = function(getApply) {
	uni.getStorage({
		key: 'student_id',
		success: (res) => {
			Vue.config.student_id = res.data;
			if (typeof getApply === "function") {
				getApply(res.data);
			}
		},
		fail: (res) => {
			uni.reLaunch({
				url: '/pages/login/login'
			})
		}
	})
}

Vue.prototype.shareFunction = function() {
	qq.showShareMenu({
		showShareItems: ['qq', 'qzone', 'wechatFriends', 'wechatMoment']
	});
	return {
		title: '工大课表（支持教务断网时查看和自定义）',
		path: '/pages/course/course',
		imageUrl: 'http://img.wh241.cn/2020/09/70af3202009140829285518.png'
	};
}

Vue.prototype.handleUrl = function(url, pc, say) {
	// #ifdef MP
	if (pc) {
		pc = "是学校官方网站，使用电脑浏览器登录体验更佳哦，它";
	} else {
		pc = "";
	}
	uni.setClipboardData({
		data: url,
		success: () => {
			uni.showModal({
				title: '温馨提示',
				content: say + pc + '的网址已经复制到剪贴板，快去浏览器粘帖吧！',
				showCancel: false,
				confirmText: '我知道了'
			});
		},
		fail: (res) => {
			uni.showModal({
				title: '温馨提示',
				content: '请使用浏览器打开网址：' + url,
				showCancel: false,
				confirmText: '我知道了'
			})
		}
	});
	// #endif
	// #ifdef H5 || APP-PLUS
	uni.navigateTo({
		url: '/pages/web/web?src=' + url + '&copy=' + (pc ? '1' : '0'),
	});
	// #endif
}

Vue.prototype.error = {};
Vue.prototype.error.internet = function() {
	uni.showToast({
		title: '网络异常',
		icon: 'none'
	});
}
Vue.prototype.error.server = function() {
	uni.showToast({
		title: '系统异常',
		icon: 'none'
	});
}
Vue.prototype.error.school = function() {
	uni.showToast({
		title: '教务异常',
		icon: 'none'
	});
}
Vue.prototype.error.login = function() {
	uni.showToast({
		title: '登陆异常',
		icon: 'none',
		duration: 2000
	});
	setTimeout(() => {
		uni.reLaunch({
			url: '/pages/login/login'
		});
	}, 2000)
}

Vue.prototype.code = {
	success: 0,
	unLogin: 2,
	unConnect: -2
}

Vue.prototype.getApply = function(id, apply, fun, flag) {
	uni.showLoading({
		title: '验证中……'
	});
	uni.request({
		url: Vue.config.baseUrl[0] + 'getapplystatus?username=' + id + '&version=' + Vue.config.version + '&platform=' +
			Vue.config.platform,
		method: 'POST',
		withCredentials: true,
		header: {
			'content-type': 'application/x-www-form-urlencoded'
		},
		success: (res) => {
			uni.hideLoading();
			if (res.statusCode == 200) {
				Vue.config.applystatus = res.data.status;
				if (typeof apply === "function") {
					apply(res.data.status);
				}

				if (typeof fun === "function") {
					if (Vue.config.applystatus == 0 || Vue.config.applystatus == 1) {
						fun();
					} else {
						uni.showModal({
							title: '提示',
							content: res.data.msg,
							showCancel: false,
							confirmText: '了解'
						});
					}
				}
				// #ifdef APP-PLUS
				if (res.data.version != Vue.config.version && flag != false) {
					uni.showModal({
						title: '更新',
						content: '目前app已经发布新版本了，请立即前往更新！',
						showCancel: true,
						success: (res) => {
							if (res.confirm) {
								uni.setStorageSync('updata', '1');
								uni.switchTab({
									url: '/pages/my/my'
								})
							}
						}
					});
				}
				// #endif
			}
		},
		fail: (res) => {
			uni.hideLoading();
			this.error.internet();
		}
	});
}

Vue.prototype.getOs_result = function(fun) {
	uni.showLoading({
		title: '加载中……'
	});
	Vue.config.cookie = uni.getStorageSync('cookie');
	uni.request({
		url: Vue.config.baseUrl[0] + 'now',
		method: 'POST',
		withCredentials: true,
		header: {
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': Vue.config.cookie
		},
		success: res => {
			uni.hideLoading();
			if (res.data.code == this.code.success) {
				Vue.config.os_result = res.data;
				uni.setStorage({
					key: 'os_result',
					data: res.data
				});
				if (typeof fun === "function") {
					fun();
				}
			} else if (res.data.code == this.code.unLogin) {
				this.error.login();
				uni.stopPullDownRefresh();
			} else {
				this.error.school();
				uni.stopPullDownRefresh();
				this.getOs_result_local(fun);
			}
		},
		fail: (res) => {
			uni.hideLoading();
			uni.stopPullDownRefresh();
			this.getOs_result_local(fun);
		}
	});
}

Vue.prototype.getOs_result_local = function(fun) {
	uni.getStorage({
		key: 'os_result',
		success: (res) => {
			Vue.config.os_result = res.data;
			if (typeof fun === "function") {
				fun();
			}
		},
		fail: (res) => {
			uni.showModal({
				title: '错误',
				content: '未获取有效数据，请在网络连接正常、教务可以正常登录后重新尝试，或联系管理员。',
				showCancel: false,
				confirmText: '了解'
			});
		}
	})
}

const app = new Vue({
	...App
})
app.$mount()
