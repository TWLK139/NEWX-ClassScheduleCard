<template>
	<view class="body">
		<view @click="goToRegister" class="canApply" v-if="applystatus == 1">
			<image style="width: 100%;height: 100%;" mode="aspectFill" src="../../static/share.jpg"></image>
			<view id="closeApply" @click.stop="closeApply">×</view>
			<view id="applyMore">点击了解详情（NEW!!!）</view>
			<view v-show="inputStudentId" @click.stop="" id="unLogin">
				<view id="untitle">免登录教务报名系统</view>
				<view>请输入学号:</view>
				<input v-model="unstudent_id" type="number" class="input inputBorder" maxlength="10" placeholder="请输入学号" />
				<view style="margin-top: 40upx;">请输入密码:</view>
				<input v-model="unpassword" class="input inputBorder" :password="true" maxlength="16" placeholder="请输入密码" />
				<view style="color: #888888;text-align: center;margin: 20upx 0upx 10upx 0upx;">
					如果始终提示密码错误请加入QQ群：726074335联系管理员
				</view>
				<button type="primary" form-type="submit" style="margin-top: 40upx;width: 90%;" @click="unlogin">提交</button>
				<view style="color: #888888;text-align: center;margin: 20upx 0;">
					如果您没有注册过，输入学号和密码后我们将为您注册并跳转登录，如果您已经注册过，我们将验证您的学号密码并登录
				</view>
			</view>
		</view>
		<view v-if="agreeShow" style="width: 100%;height: 100%;position: fixed;top: 0;left: 0;z-index: 10000;background-color: rgba(0, 0, 0, 0.5);">
			<view style="height:400upx" class="canApply urgent">
				<view id="untitle" style="position: fixed;top: 0;">提示</view>
				<view id="untitle"></view>
				<view style="width: 90%;height: 200upx;overflow: scroll;margin: 0 auto;font-size: 45upx;">
					本小程序致力于为学生提供便利，方便学生查看信息，可以在本地设置课程数据，以免遗忘。<br>本小程序郑重承诺不会保留任何用户信息，因此不存在从本小程序服务器泄露用户数据的可能性。当前本小程序为内部测试阶段，仅限受邀请的用户登录，请勿传播。
					<view v-if="applystatus == 2">请输入邀请码：</view>
					<input v-model="invitation" v-if="applystatus == 2" class="input inputBorder" :password="true" maxlength="16"
					 placeholder="请输入邀请码" />
				</view>
				<button type="primary" form-type="submit" @click="agreeShow = false" :disabled="applystatus == 2 && invitation != 'NEWX1234'">同意</button>
				<!--  -->
			</view>
		</view>
		<form @submit="formSubmit">
			<view class="face-wapper">
				<image src="../../static/registLogin/default-face.png" class="face"></image>
			</view>

			<view class="info-wapper">
				<label class="words-lbl">学号</label>
				<input name="username" type="text" value="" v-model="username" class="input" placeholder="请输入学号" />
			</view>

			<view class="info-wapper" style="margin-top: 40upx;">
				<label class="words-lbl" onpaste="return false;">密码</label>
				<input name="password" type="text" value="" v-model="password" :password="PWShow" class="input" placeholder="请输入教务密码" />
				<image class="pwEye" @click="PWShow = !PWShow" v-if="!PWShow" src="../../static/login/openeye.png"></image>
				<image class="pwEye" @click="PWShow = !PWShow" v-else src="../../static/login/closeeye.png"></image>
			</view>
			<view style="width: 600upx;margin-top: 30upx;" class="question">
				<text class="cuIcon-question"></text>
				注：密码为教务信息管理系统密码，默认为学号
				<view style="width: 100%;display: flex;flex-direction: row;justify-content: center;color: #8799A3;">
					<view @click="handleUrl('http://my.hfut.edu.cn/getPasswordChangeLinkByMail.portal&copy=1', true, '合肥工业大学教务密码修改系统')">忘记密码</view>
					<view @click="handleUrl('http://jxglstu.hfut.edu.cn/eams5-student/login&copy=1', true, '合肥工业大学教务系统')" style="margin-left: 60upx;">前往教务</view>
				</view>
			</view>
			<button type="primary" form-type="submit" style="margin-top: 20upx;width: 90%;">登录</button>
			<view class="gotoQuery" @click="gotoQuery">体验查课功能</view>
			<navigator class="gotoQuery" url="../list/list">查看用户手册</navigator>
		</form>
	</view>
</template>

<script>
	import Vue from 'vue';
	export default {
		data() {
			return {
				PWShow: true,
				username: '',
				password: '',
				applystatus: -1,
				unstudent_id: '',
				unpassword: '',
				inputStudentId: false,
				invitation: '',
				agreeShow: true
			};
		},
		onBackPress() {
			// #ifdef APP-PLUS  
			plus.runtime.quit();
			// #endif

			return true
		},
		onLoad() {
			uni.request({
				url: Vue.config.baseUrl[0] + 'getapplystatus',
				method: 'POST',
				withCredentials: true,
				header: {
					'content-type': 'application/x-www-form-urlencoded'
				},
				success: res => {
					uni.hideLoading();
					this.applystatus = res.data.status;
				},
				fail: res => {
					uni.hideLoading();
					uni.showModal({
						title: '提示',
						content: '请检查网络连接',
						showCancel: false,
						confirmText: '了解'
					});
				}
			});
			uni.hideLoading();
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
					if (res.data.code == this.code.success) {
						uni.setStorage({
							key: 'os_result',
							data: res.data
						});
					} else if (res.data.code == this.code.unLogin) {
						uni.removeStorage({
							key: 'student_id',
						});
					}
				},
				fail: function(res) {
					this.error.internet();
				}
			});
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			formSubmit: function(e) {
				uni.showLoading({
					title: '登录中……'
				});
				var value = JSON.stringify(e.detail.value);
				if (this.username == '') {
					uni.hideLoading();
					uni.showToast({
						title: '请输入学号',
						icon: 'none'
					});
					return;
				} else if (this.password == '') {
					uni.hideLoading();
					uni.showToast({
						title: '请输入密码',
						icon: 'none'
					});
					return;
				}
				uni.request({
					url: Vue.config.baseUrl[0] + 'login',
					method: 'POST',
					withCredentials: true,
					header: {
						'content-type': 'application/x-www-form-urlencoded'
					},
					data: {
						username: this.username,
						password: this.password,
					},
					success: res => {
						if (res.data.code == this.code.success || res.data.code == 3) {
							if (res.header['Set-Cookie']) {
								uni.setStorageSync('cookie', res.header['Set-Cookie'].split(';')[0]);
								Vue.config.cookie = res.header['Set-Cookie'].split(';')[0];
							} else if (res.header['set-cookie']) {
								uni.setStorageSync('cookie', res.header['set-cookie'].split(';')[0]);
								Vue.config.cookie = res.header['set-cookie'].split(';')[0];
							} else {
								uni.setStorageSync('cookie', '');
							}
							uni.request({
								url: Vue.config.baseUrl[0] + 'kick',
								method: 'POST',
								withCredentials: true,
								header: {
									'content-type': 'application/x-www-form-urlencoded',
									'cookie': Vue.config.cookie
								},
								success: res => {
									uni.hideLoading();
									if (res.data.code == this.code.success) {
										uni.showToast({
											title: '登录成功',
											icon: 'none'
										});

										uni.setStorageSync('student_id', this.username);

										uni.switchTab({
											url: '/pages/course/course'
										});
									} else if (res.data.code == this.code.unLogin) {
										this.error.server();
									} else {
										this.error.school();
									}
								},
								fail: res => {
									uni.hideLoading();
									this.error.internet();
								}
							});
						} else {
							uni.hideLoading();
							uni.showToast({
								title: res.data.msg,
								icon: 'none'
							});
						}
					}
				});
			},
			goToRegister() {
				uni.showLoading({
					title: '验证中……'
				});
				uni.request({
					url: Vue.config.baseUrl[0] + 'getapplystatus',
					method: 'POST',
					withCredentials: true,
					header: {
						'content-type': 'application/x-www-form-urlencoded'
					},
					success: res => {
						uni.hideLoading();
						if (res.data.status == 1) {
							this.inputStudentId = true;
						} else if (res.data.status == 0) {
							uni.showModal({
								title: '提示',
								content: '请先登录',
								showCancel: false,
								confirmText: '了解'
							});
							this.applystatus = -1
						} else {
							uni.showModal({
								title: '提示',
								content: res.data.msg,
								showCancel: false,
								confirmText: '了解'
							});
						}
					},
					fail: res => {
						uni.hideLoading();
						uni.showModal({
							title: '提示',
							content: '请检查网络连接',
							showCancel: false,
							confirmText: '了解'
						});
					}
				});
			},
			unlogin() {
				if (this.unstudent_id.length != 10) {
					uni.showToast({
						title: '学号格式错误',
						icon: 'none'
					});
				} else if (this.unpassword.length < 6) {
					uni.showToast({
						title: '密码需大于六位',
						icon: 'none'
					});
				} else {
					uni.showLoading({
						title: '验证中……'
					});
					uni.request({
						url: Vue.config.baseUrl[3] + 'applogin?username=' + this.unstudent_id + '&password=' + this.unpassword,
						method: 'GET',
						success: res => {
							uni.hideLoading();
							if (res.data.code == this.code.success) {
								uni.setStorageSync('student_id', this.unstudent_id);
								uni.setStorageSync('user_id' + this.unstudent_id, res.data.data.id);
								uni.navigateTo({
									url: '../apply/apply'
								});
							} else {
								uni.showModal({
									title: '错误',
									content: res.data.msg,
									showCancel: false,
									confirmText: '了解'
								});
							}
						},
						fail: (res) => {
							uni.hideLoading();
							uni.showModal({
								title: '提示',
								content: '请检查网络',
								showCancel: false,
								confirmText: '了解'
							})
						}
					});
				}

			},
			closeApply() {
				uni.showModal({
					title: '提示',
					content: '大学生网络文化工作室是宣城校区校级学生组织，这里有着优良的学术交流氛围，欢迎您的到来！（关闭后可在“我的”页面“NEWX分享会”中查看）',
					showCancel: false,
					confirmText: '关闭',
					success: res => {
						this.applystatus = -1;
					}
				});
			},
			gotoQuery() {
				uni.switchTab({
					url: '../query/query'
				});
			}
		},
		onLaunch: function() {}
	};
</script>

<style>
	@import './registLogin.css';

	.question {
		margin: 0 auto;
		font-size: 15px;
		width: 400rpx;
	}

	.gotoQuery {
		width: 100%;
		text-align: center;
		margin-top: 40upx;
		font-size: 30upx;
		color: #828F9A;
	}
</style>
