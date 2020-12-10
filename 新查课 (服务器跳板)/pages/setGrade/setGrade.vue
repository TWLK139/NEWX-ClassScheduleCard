<template>
	<view>
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view id="title" @click="ask()">
			<view>课程名</view>
			<image id="ask_image" mode="widthFix" src="../../static/grade/ask.png"></image>
			<view class="title_word_right">必修 | 辅修 | 选修</view>
		</view>
		<view class="box_grade" style="margin-top: 12%;" v-for="(theTrem, index) in grade_res" :key="grade_res[index].code">
			<view class="flex_box_grade">
				<view class="trem_name">{{ grade_res[index].name }}</view>
			</view>

			<view class="detail_box_lesson" v-for="(lesson, inLe) in grade_res[index].lessons" :key="inLe">
				<view class="flex_box_detail">
					<view class="ellipsis_detail_box">{{ lesson.course_name }}</view>
				</view>
				<view class="title_word_right">
					<view class="choose_box" @click="setSet(grade_res[index].lessons[inLe].course_code, 0)">必
						<image v-show="returnSet(grade_res[index].lessons, inLe) == 0" class="choose_img" src="../../static/choose.png"></image>
					</view>
					<view>|</view>
					<view class="choose_box" @click="setSet(grade_res[index].lessons[inLe].course_code, 1)">辅
						<image v-show="returnSet(grade_res[index].lessons, inLe) == 1" class="choose_img" src="../../static/choose.png"></image>
					</view>
					<view>|</view>
					<view class="choose_box" @click="setSet(grade_res[index].lessons[inLe].course_code, 2)">选
						<image v-show="returnSet(grade_res[index].lessons, inLe) == 2" class="choose_img" src="../../static/choose.png"></image>
					</view>
				</view>
			</view>
		</view>
		<view id="saveButton" @click="saveSet()">保存</view>
		<view style="width: 100%;height: 200upx;"></view>
	</view>
</template>

<script>
	import Vue from 'vue';
	export default {
		data() {
			return {
				grade_res: [],
				isRequire: {},
				flag: true,
				course_num: {},
				student_id: ''
			};
		},
		onLoad() {
			uni.getStorage({
				key: 'student_id',
				success: res => {
					this.student_id = res.data;
					this.getMessage();
				},
				fail() {
					uni.navigateTo({
						url: '../login/login'
					});
				}
			});
		},
		onBackPress(event) {
			if (event.from == 'navigateBack') return false;
			if (Object.keys(this.course_num).length != Object.keys(this.isRequire).length) {
				uni.showModal({
					title: '未完成',
					content: '存在未设置的课程，请完善设置后再返回',
					showCancel: true,
					confirmText: '继续设置',
					cancelText: '以后再说',
					success: res => {
						if (res.cancel) {
							uni.setStorage({
								key: 'grade_isRequire' + this.student_id,
								data: this.isRequire,
								complete() {
									uni.navigateTo({
										url: '../grade/grade'
									});
								}
							});
						}
					}
				});
			} else {
				uni.showLoading({
					mask: true,
					title: '正在保存'
				});
				uni.setStorage({
					key: 'grade_isRequire' + this.student_id,
					data: this.isRequire,
					success: res => {
						uni.hideLoading();
						uni.showToast({
							title: '保存成功'
						});
						uni.navigateTo({
							url: '../grade/grade'
						});
					},
					fail: res => {
						uni.showToast({
							title: '保存失败',
							icon: 'none'
						});
					}
				});
			}
			return true;
		},
		onShow() {
			this.simpleCheck();
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			getMessage() {
				uni.showLoading({
					title: '加载中',
					mask: true
				});
				Vue.config.cookie = uni.getStorageSync('cookie');
				uni.request({
					url: Vue.config.baseUrl[0] + 'score',
					method: 'POST',
					withCredentials: true,
					header: {
						'content-type': 'application/x-www-form-urlencoded',
						'cookie': Vue.config.cookie
					},
					data: {
						semestercode: 'all'
					},
					success: res => {
						uni.hideLoading();
						if (res.data.code == this.code.success) {
							this.grade_res = res.data.data;
							uni.setStorage({
								key: 'grade_res' + this.student_id,
								data: res.data.data
							});
							this.getSet();
						} else if (res.data.code == this.code.unLogin) {
							this.error.login();
						} else {
							this.error.school();
							uni.getStorage({
								key: 'grade_res' + this.student_id,
								success: (res) => {
									this.grade_res = res.data;
									this.getSet();
									uni.hideLoading();
								}
							});
						}
					},
					fail: res => {
						this.error.internet();
						uni.getStorage({
							key: 'grade_res' + this.student_id,
							success: (res) => {
								this.grade_res = res.data;
								this.getSet();
								uni.hideLoading();
							}
						});
					}
				});
			},
			getSet() {
				uni.getStorage({
					key: 'grade_isRequire' + this.student_id,
					success: res => {
						this.isRequire = res.data;
						this.getCourseNum()
					},
					fail: res => {
						this.isRequire = {};
						this.getCourseNum()
					},
					complete: (res) => {
						this.$forceUpdate();
					}
				});
			},
			setSet(index, res) {
				this.flag = !this.flag;
				this.isRequire[index] = res;
			},
			getCourseNum() {
				for (var i = 0; i < this.grade_res.length; i++) {
					for (var j = 0; j < this.grade_res[i].lessons.length; j++) {
						this.course_num[this.grade_res[i].lessons[j].course_code] = 1;
						var tem = this.grade_res[i].lessons[j].course_code;
						if (this.isRequire[tem] == null) {
							if (tem.substr(tem.length - 1, 1) == 'B') {
								this.isRequire[tem] = 0;
							} else if (tem.substr(tem.length - 1, 1) == 'M') {
								this.isRequire[tem] = 2;
							}
						}
					}
				}
				this.flag = !this.flag;
				if (Object.keys(this.course_num).length != Object.keys(this.isRequire).length) {
					this.ask();
				}
			},
			saveSet() {
				uni.setStorage({
					key: 'grade_isRequire' + this.student_id,
					data: this.isRequire,
					success: res => {
						uni.hideLoading();
						uni.showToast({
							title: '保存成功'
						});
						if (Object.keys(this.course_num).length == Object.keys(this.isRequire).length) {
							uni.navigateTo({
								url: '../grade/grade'
							})
						}
					},
					fail: res => {
						uni.showToast({
							title: '保存失败',
							icon: 'none'
						});
					}
				});
			},
			ask() {
				uni.showModal({
					title: '提示',
					content: '部分课程设置了默认属性，您需要完善未设置默认属性的课程，同时请您务必注意您辅修的课程属性，因为它可能会被错误地归为必修',
					showCancel: false,
					confirmText: '了解'
				})
			}
		},
		computed: {
			returnSet() {
				return function(ob, index) {
					if (this.flag || !this.flag) {
						if (ob.length > index) {
							if (this.isRequire[ob[index].course_code] == 0) {
								return 0;
							} else if (this.isRequire[ob[index].course_code] == 1) {
								return 1;
							} else if (this.isRequire[ob[index].course_code] == 2) {
								return 2;
							} else {
								return -1;
							}
						}
					}
				};
			}
		}
	};
</script>

<style>
	@import url('./setGrade.css');
</style>
