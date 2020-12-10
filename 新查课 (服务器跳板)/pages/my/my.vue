<template>
	<view>
		<view class="statusBar" :style="{height:statusBarHeight+'px'}"></view>
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view id="main" :style="{marginTop:statusBarHeight+'px'}">
			<view id="firstPage" class="firstpage" style="position: relative;">
				<view @click="handleUrl('http://www.hfut.edu.cn', false, '合肥工业大学')" id="schoolLogo">
					<image mode="widthFix" style="width: 100%;height: 100%;" src="../../static/my/hfutLogo.png">
				</view>
				<view @click="handleUrl('http://mobile.newxstudio.com', false, '大学生网络文化工作室')" class="newxLogo" id="newxLogo">
					<image mode="widthFix" src="../../static/my/newxLogo.png">
				</view>
				<image id="leftimg" src="../../static/registLogin/default-face.png"></image>
				<p id="name">你好，</br>{{ mes.user_name }}</p>
				<p id="slogan">青春 / 自信 / 技术宅</p>
				<view class="rightimg" id="rightimg" @click="handleUrl('http://mobile.newxstudio.com', false, '合肥工业大学宣城校区大学生网络文化工作室官方网站网址')">
					<image mode="widthFix" style="width: 100%;" src="../../static/my/newxBack.png">
				</view>
			</view>
		</view>
		<view id="message" :style="{height:mes_height_compute+'px'}">
			<view id="mes_title" @click="showMessage()">
				<image style="position: absolute;left: 40upx;margin: 0;" class="icon_img" src="../../static/my/message.png"></image>
				<view id="mse_title">我的信息</view>
				<image :style="{transform: 'rotate('+mes_rotate+'deg)'}" class="icon_open" src="../../static/my/next.png"></image>
			</view>
			<view class="mes_con_box">
				<view class="mes_con_title">学号</view>
				<view class="mes_con_con">{{mes.user_code}}</view>
			</view>
			<view class="mes_con_box">
				<view class="mes_con_title">学院</view>
				<view class="mes_con_con">{{mes.depart_name}}</view>
			</view>
			<view class="mes_con_box">
				<view class="mes_con_title">专业</view>
				<view class="mes_con_con">{{mes.major_name}}</view>
			</view>
			<view class="mes_con_box">
				<view class="mes_con_title">班级</view>
				<view class="mes_con_con">{{mes.adminclass_name}}</view>
			</view>
			<view class="mes_con_box">
				<view class="mes_con_title">电话</view>
				<view class="mes_con_con">{{mes.mobile_phone}}</view>
			</view>
			<view class="mes_con_box">
				<view class="mes_con_title">邮箱</view>
				<view class="mes_con_con">{{mes.account_email}}</view>
			</view>
			<view class="mes_con_box">
				<view class="mes_con_title">性别</view>
				<view class="mes_con_con">{{mes.gender}}</view>
			</view>
			<view class="mes_con_box">
				<view class="mes_con_title">生日</view>
				<view class="mes_con_con">{{mes.birthday}}</view>
			</view>
		</view>
		<view id="but_box">
			<navigator class="but" url="../grade/grade">
				<image class="icon_img" src="../../static/my/grade.png"></image>
				<view class="word">查询成绩</view>
				<image class="icon_open" src="../../static/my/next.png"></image>
			</navigator>
			<navigator class="but" url="../test/test">
				<image class="icon_img" src="../../static/my/test.png"></image>
				<view class="word">考试信息</view>
				<image class="icon_open" src="../../static/my/next.png"></image>
			</navigator>
			<navigator class="but" url="../classSave/classSave">
				<image class="icon_img" src="../../static/my/lessonSave.png"></image>
				<view class="word">收藏课程</view>
				<image class="icon_open" src="../../static/my/next.png"></image>
			</navigator>
			<navigator class="but" url="../list/list">
				<image class="icon_img" src="../../static/my/userHelp.png"></image>
				<view class="word">用户手册</view>
				<image class="icon_open" src="../../static/my/next.png"></image>
			</navigator>
			<!-- #ifdef APP-PLUS -->
			<view class="but" @click="upgrade">
				<image class="icon_img" src="../../static/my/updata.png"></image>
				<view class="word">软件更新</view>
				<image class="icon_open" src="../../static/my/next.png"></image>
			</view>
			<!-- #endif -->
			<navigator class="but" url="../about/about">
				<image class="icon_img" src="../../static/my/about.png"></image>
				<view class="word">关于我们</view>
				<image class="icon_open" src="../../static/my/next.png"></image>
			</navigator>
			<view v-if="applystatus == 0 || applystatus == 1" class="but" @click="goToRegister()">
				<image class="icon_img" src="../../static/my/join.png"></image>
				<view class="word">NEWX分享会</view>
				<image class="icon_open" src="../../static/my/next.png"></image>
			</view>
			<view class="but" @click="checkOnline(deleteStorage)">
				<image class="icon_img" src="../../static/my/clean.png"></image>
				<view class="word">清除缓存</view>
				<image class="icon_open" src="../../static/my/next.png"></image>
			</view>
			<view class="but" @click="checkOnline(signOut)">
				<image class="icon_img" src="../../static/my/exit.png"></image>
				<view class="word">退出登录</view>
				<image class="icon_open" src="../../static/my/next.png"></image>
			</view>
		</view>

		<view style="width: 100%;height: 80upx;"></view>

		<view class="download" v-show="upgradeHidden == false">
			<uni-popup ref="popup" type="center" :maskClick="false">
				<view class="upgrade">
					<view class="content">
						<view class="title">
							<text>{{upgrading?"正在升级":"发现新版本:"+newVersion.v2}}</text>
						</view>
						<view class="container">
							<view class="descriptions">
								<text>{{upgrading?"正在为您下载,请耐心等待":"本次版本更新描述内容:"}}</text>
							</view>
							<view class="details" v-if="!upgrading">
								<view class="item" v-for="(upd, i) in newVersion.content" :key="i">
									<text>{{ i+1 }}：{{ upd }}</text>
								</view>
							</view>
							<view v-else class="prpgroess">
								<progress :percent="downloadTime" active-mode="forwards" activeColor="red" active stroke-width="4" show-info />
							</view>
						</view>
						<view v-if="!upgrading" class="btn-group">
							<view class="cancel" @click="hiddenUppop">
								<text>取消</text>
							</view>
							<view class="confirm" @click="upgradeEvent">
								<text>确定</text>
							</view>
						</view>
						<view v-else class="btn-group">
							<view v-if="!isForceUpgrade" class="cancel" @click="abortDownload">
								<text>取消下载</text>
							</view>
						</view>
					</view>
				</view>
			</uni-popup>
		</view>
	</view>
</template>

<script>
	import Vue from 'vue';
	import uniPopup from "../updatepage/uni-popup/uni-popup.vue";
	import uniPopupMessage from "../updatepage/uni-popup/uni-popup-message.vue";
	import uniPopupDialog from "../updatepage/uni-popup/uni-popup-dialog.vue";
	export default {
		data() {
			return {
				mes: {},
				intrBut: '了解更多',
				statusBarHeight: '',
				mes_height: 600,
				mes_rotate: -90,
				student_id: '',
				touchStartData: {
					sx: 0,
					ex: 0,
					sy: 0,
					ey: 0
				},
				applystatus: -1,


				newVersion: 0,
				// 是否更新
				upgrading: false,
				upgradeHidden: false,
				// 下载时间
				downloadTime: 0,
				// 定时器
				timer: null,
				// 是否强制更新
				isForceUpgrade: false,
				// 下载任务
				downloadTask: null,
				// 下载地址
				downloadUrl: "http://newx.huii.top/app/newx",
			};
		},
		onLoad(option) {
			this.student_id = uni.getStorageSync('student_id')
			this.getMessage();

			setTimeout(() => {
				uni.getSystemInfo({
					success: (res) => {
						this.statusBarHeight = res.statusBarHeight;
					}
				})
			}, 10);
		},
		onShow() {
			this.simpleCheck((id) => {
				this.student_id = Vue.config.student_id;
				this.getApply(id, (res) => {
					this.applystatus = res;
				}, null, false);
			});
			if (uni.getStorageSync('updata') == 1) {
				uni.removeStorageSync('updata');
				this.upgrade();
			}
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			showMessage() {
				if (this.mes_height == 80) {
					this.mes_height = 600;
					this.mes_rotate = -90;
				} else {
					this.mes_height = 80;
					this.mes_rotate = 90;
				}
			},
			getMessage() {
				uni.showLoading({
					title: '加载中……'
				});
				uni.getStorage({
					key: 'my_mes' + this.student_id,
					success: (res) => {
						this.mes = res.data;
					},
					complete: (res) => {
						Vue.config.cookie = uni.getStorageSync('cookie');
						uni.request({
							url: Vue.config.baseUrl[0] + 'info',
							method: 'POST',
							withCredentials: true,
							header: {
								'content-type': 'application/x-www-form-urlencoded',
								'cookie': Vue.config.cookie
							},
							success: (res) => {
								if (res.data.code == this.code.success) {
									this.mes = res.data.data;
									this.$forceUpdate();
									uni.setStorage({
										key: 'my_mes' + this.student_id,
										data: res.data.data,
									});
								} else if (res.data.code == this.code.unLogin) {
									this.error.login();
								} else {
									this.error.school();
								}
							},
							fail: (res) => {
								this.error.internet();
							},
							complete: (res) => {
								uni.hideLoading();
							}
						})
					}
				});
			},
			deleteStorage() {
				uni.showModal({
					title: '请确认',
					content: '您确定要删除缓存数据？警告：删除后所有自定义课程、备忘录等内容都将丢失，且无法找回（教务上存在的数据联网后可再次获取）。',
					showCancel: true,
					cancelText: '点错了',
					confirmText: '确定',
					confirmColor: '#DD514C',
					cancelColor: '#0FB045',
					success: (res) => {
						if (res.confirm) {
							uni.showLoading({
								title: '删除中……'
							});
							uni.clearStorage({
								success: (res) => {
									uni.setStorage({
										key: 'student_id',
										data: this.student_id,
										success: (res) => {
											uni.showToast({
												title: '删除成功！'
											});
										},
										fail: (res) => {
											uni.showToast({
												title: '故障！可能需要重新登录！',
												icon: 'none'
											});
										}
									});
								},
								fail: (res) => {
									uni.showToast({
										title: '清理失败！',
										icon: 'none'
									});
								},
								complete: (res) => {
									uni.hideLoading();
								}
							});
						}
					}
				});
			},
			goToRegister() {
				if (this.applystatus == 0 || this.applystatus == 1) {
					uni.request({
						url: Vue.config.baseUrl[3] + "applogin?username=" + this.student_id,
						method: 'GET',
						success: (res) => {
							if (res.data.code == this.code.success) {
								uni.setStorageSync("user_id" + this.student_id, res.data.data.id);
								uni.navigateTo({
									url: '../apply/apply'
								});
							} else {
								this.error.server();
							}
						},
						fail: (res) => {
							this.error.internet();
						}
					})
				} else {
					uni.showModal({
						title: '提示',
						content: '报名暂未开放。',
						showCancel: false,
						confirmText: '了解'
					});
				}
			},
			signOut() {
				uni.showModal({
					title: '请确认',
					content: '您确定要退出？提示：退出后不会删除您自定义的数据，但如果教务闭网则可能导致您无法登录。',
					showCancel: true,
					cancelText: '点错了',
					confirmText: '确定',
					confirmColor: '#DD514C',
					cancelColor: '#0FB045',
					success: (res) => {
						if (res.confirm) {
							Vue.config.cookie = uni.getStorageSync('cookie');
							uni.request({
								url: Vue.config.baseUrl[0] + 'logout',
								method: 'POST',
								withCredentials: true,
								header: {
									'content-type': 'application/x-www-form-urlencoded',
									'cookie': Vue.config.cookie
								},
								complete: (res) => {
									uni.removeStorage({
										key: 'student_id',
										complete: (res) => {
											uni.reLaunch({
												url: '/pages/login/login'
											});
										}
									});
								}
							});
						}
					}
				});
			},
			checkOnline(myFun) {
				uni.showLoading({
					title: '检查网络……'
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
					success: (res) => {
						if (res.data.code == this.code.success) {
							myFun();
						} else if (res.data.code == this.code.unLogin) {
							uni.reLaunch({
								url: '/pages/login/login'
							});
						} else {
							uni.showModal({
								title: '警告',
								content: '检查到当前网络异常，建议不要执行该操作。因为如果教务系统出现异常，将导致您无法再获取到任何信息。',
								showCancel: true,
								confirmText: '仍然执行',
								cancelText: '暂不执行',
								success: (res) => {
									if (res.confirm) {
										myFun();
									}
								}
							});
						}
					},
					fail: (res) => {
						uni.showModal({
							title: '警告',
							content: '检查到当前网络异常，建议不要执行该操作。因为如果教务系统出现异常，将导致您无法再获取到任何信息。',
							showCancel: true,
							confirmText: '仍然执行',
							cancelText: '暂不执行',
							success: (res) => {
								if (res.confirm) {
									myFun();
								}
							}
						});
					},
					complete: (res) => {
						uni.hideLoading();
					}
				});

			},
			// #ifdef APP-PLUS
			// 取消更新
			hiddenUppop() {
				this.$refs.popup.close();
			},
			// 检测更新
			upgrade() {
				if (this.upgradeHidden) {
					this.upgradeHidden = false;
				} else {
					uni.showLoading({
						title: '加载中……'
					});
					uni.request({
						url: Vue.config.baseUrl[0] + 'getupdate',
						success: (res) => {
							uni.hideLoading();
							if (res.data.data.v1 != Vue.config.version) {
								this.newVersion = res.data.data;
								this.newVersion.content = this.newVersion.content.split("%");
								this.$refs.popup.open();
							} else {
								uni.showModal({
									title: '提示',
									content: '目前app已经是最新版本了',
									showCancel: false,
								})
							}
						},
						fail: (res) => {
							uni.hideLoading();
							this.error.internet();
						}
					})
				}
			},
			// 点击更新
			upgradeEvent() {
				if (!this.upgrading) {
					this.upgrading = true;
					// 如果是强制更新
					this.isForceUpgrade = false;
					this.downloadApplications();
				}
			},
			// 后台下载
			hiddenUpgradeEvent() {
				this.$refs.popup.close();
				this.upgradeHidden = true;
			},
			// 下载
			downloadApplications() {
				// 建立下载任务
				this.downloadTask = uni.downloadFile({
					// 下载地址
					url: this.newVersion.url,
					success: (res) => {
						if (res.statusCode == 200) {
							// 把当前app保存下载
							uni.saveFile({
								tempFilePath: res.tempFilePath,
								success: (resp) => {
									plus.runtime.install(resp.savedFilePath);
								},
								fail: (err) => {
									// 保存失败
									uni.showModal({
										title: '失败',
										content: '安装失败，请联系管理员',
										showCancel: false
									});
								}
							});
						}
					},
				});
			
				this.downloadTask.onProgressUpdate((res) => {
					// 下载进度
					this.downloadTime = res.progress;
				});
			},
			// 取消下载
			abortDownload() {
				this.downloadTime = 0;
				if (this.$refs.popup) {
					this.$refs.popup.close();
					setTimeout(() => {
						this.upgrading = false;
					}, 200);
				}
			
				clearInterval(this.timer);
				if (this.downloadTask) {
					this.downloadTask.abort();
				}
			},
			// #endif
		},
		computed: {
			mes_height_compute() {
				return uni.upx2px(this.mes_height);
			}
		},
		components: {
			uniPopup,
			uniPopupMessage,
			uniPopupDialog,
		}
	}
</script>

<style>
	@import url("./my.css");

	/* #ifdef APP-PLUS */
	.download .logo {
		width: 208rpx;
	}

	.download .upgrade {
		position: relative;
		background: #fff;
		width: 468rpx;
		min-height: 238rpx;
		border-radius: 20rpx;
	}

	.download .logo image {
		width: 208rpx;
		position: absolute;
		top: -80rpx;
		left: 0;
		right: 0;
		margin: 0 auto;
	}

	.download .content {
		padding-top: 80rpx;
	}

	.download .content .title {
		text-align: center;
		font-size: 30rpx;
		font-weight: bold;
	}

	.download .content .container {
		color: #666;
	}

	.download .content .container .descriptions {
		padding: 0rpx 30rpx;
		text-align: center;
		font-size: 28rpx;
	}

	.download .content .container .details,
	.download .content .prpgroess {
		padding: 16rpx 46rpx;
		box-sizing: border-box;
		font-size: 24rpx;
	}

	.download .content .prpgroess {
		padding: 16rpx 22rpx;
		margin: 20rpx 0;
	}

	.download .content .btn-group {
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.download .content .btn-group view {
		width: 200rpx;
		height: 68rpx;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 14rpx;
		font-size: 24rpx;
		border-radius: 16rpx;
		line-height: 1.5;
	}

	.download .content .btn-group view:last-child {
		background: #ef5656;
		color: #fff;
	}

	/* #endif */
</style>
