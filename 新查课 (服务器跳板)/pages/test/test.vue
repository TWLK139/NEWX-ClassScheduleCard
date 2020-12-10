<template>
	<view>
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view :class="['box_grade', returnTremShow(index) ? '' : 'choose_heght_min_min']" v-for="(trem, index) in trem_res"
		 :key="trem.code">
			<view class="flex_box_grade">
				<view class="trem_name" @click="ask()">{{ trem.name }}</view>
				<image class="ask_image" mode="widthFix" src="../../static/grade/ask.png" @click="ask()"></image>
				<view class="trem_season" :class="[trem.season == '春' ? 'choose_grass' : 'choose_harvest']" @click="showEvent(index)">({{ trem.season }})</view>
				<image :class="['image_grade', returnTremShow(index) ? 'choose_minus90' : 'choose_90']" src="../../static/next.png"
				 @click="showEvent(index)"></image>
			</view>
			<view v-if="exam_detail_show[trem.code] == null" class="click_load_button" @click="loadMessage(trem.code)">点击加载</view>
			<view v-else-if="exam_online[trem.code].length == 0 && exam_local[trem.code].length == 0" class="click_load_button">暂时没有数据哦</view>

			<view :class="['exam_detail_box', returnHeightL(trem.code, index) == 1 ? 'choose_heght_min' : returnHeightL(trem.code, index) == 2 ? '' : 'choose_heght_mid']"
			 v-for="(exam, index) in exam_local[trem.code]" v-if="exam_detail_show[trem.code] != null" :key="index">
				<view class="flex_exam_box" @click="editEvent(2, trem.code, index)">
					<view class="exam_icon" :style="{ backgroundColor: colors[exam.title_color] }">{{ exam.title_word }}</view>
					<view class="exam_name">{{ exam.course_name }}</view>
					<view class="exam_type">{{ exam.exam_type }}</view>
					<image class="exam_edit_img" mode="widthFix" src="../../static/test/edit.png"></image>
				</view>
				<view class="flex_exam_box exam_mes_word" @click="showDetailL(trem.code, index)">
					<view class="flex_exam_box_con">
						<view class="exam_mes_word_title">日期:</view>
						<view>{{ exam.date }}</view>
					</view>
					<view class="flex_exam_box_con" style="justify-content: right;">
						<view class="exam_mes_word_title">时间:</view>
						<view>{{ exam.time_start }} - {{ exam.time_end }}</view>
					</view>
				</view>
				<view class="flex_exam_box exam_mes_word" style="padding-bottom: 10upx;">
					<view class="exam_box_con" style="width: 75%;" @click="showDetailL(trem.code, index)">
						<view class="exam_mes_word_title exam_mes_place">地点:</view>
						<view class="exam_mes_place">{{ exam.room_name }}</view>
					</view>
					<view class="flex_exam_box_con" style="width: 25%;justify-content: space-between;">
						<view class="flex_exam_box_con choose_unfinish" @click="showDetailL(trem.code, index)">备注</view>
						<view :class="['flex_exam_box_con', 'choose_unfinish', returnHeightL(trem.code, index) == 1 ? 'choose_finished' : '']"
						 @click="makeDoneL(trem.code, index)">
							{{ returnHeightL(trem.code, index) == 1 ? '已完成' : '待做' }}
						</view>
					</view>
				</view>
				<view class="exam_more" style="margin-bottom:15upx">备注：{{ local_more[trem.code][index] }}</view>
			</view>

			<view v-if="exam_detail_show[trem.code] != null" v-for="(exam, index) in exam_online[trem.code]" :key="index" :class="['exam_detail_box', returnHeight(trem.code, index, exam.lesson_code) == 1 ? 'choose_heght_min' : returnHeight(trem.code, index, exam.lesson_code) == 2 ? '' : 'choose_heght_mid']">
				<view class="flex_exam_box" @click="editEvent(1, trem.code, index, exam!=undefined?exam.lesson_code:-1)">
					<view class="exam_icon">考试</view>
					<view class="exam_name">{{ exam.course_name }}</view>
					<view class="exam_type">{{ exam.exam_type }}</view>
					<image class="exam_edit_img" mode="widthFix" src="../../static/test/edit.png"></image>
				</view>
				<view class="flex_exam_box exam_mes_word" @click="showDetail(trem.code, index)">
					<view class="flex_exam_box_con">
						<view class="exam_mes_word_title">日期:</view>
						<view>{{ exam.date }}</view>
					</view>
					<view class="flex_exam_box_con" style="justify-content: right;">
						<view class="exam_mes_word_title">时间:</view>
						<view>{{ exam.time_start }} - {{ exam.time_end }}</view>
					</view>
				</view>
				<view class="flex_exam_box exam_mes_word" style="padding-bottom: 10upx;">
					<view class="exam_box_con" style="width: 75%;" @click="showDetail(trem.code, index)">
						<view class="exam_mes_word_title exam_mes_place">地点:</view>
						<view class="exam_mes_place">{{ exam.room_name }}</view>
					</view>
					<view class="flex_exam_box_con" style="width: 25%;justify-content: space-between;">
						<view class="flex_exam_box_con choose_unfinish" @click="showDetail(trem.code, index)">备注</view>
						<view @click="makeDone(trem.code, exam!=undefined?exam.lesson_code:-1)" :class="['flex_exam_box_con', 'choose_unfinish', returnHeight(trem.code, index, exam.lesson_code) == 1 ? 'choose_finished' : '']">
							{{ returnHeight(trem.code, index, exam.lesson_code) == 1 ? '已完成' : '待做' }}
						</view>
					</view>
				</view>
				<view class="exam_more">课程代码：{{ exam.lesson_code }}</view>
				<view class="exam_more" style="margin-bottom:15upx">备注：{{ exam_more[trem.code][exam.lesson_code] }}</view>
			</view>

		</view>
		<view id="saveButton" @click="editEvent(0, '', 0)">添加事件</view>
		<view style="width: 100%;height: 200upx;"></view>
	</view>
</template>

<script>
	import Vue from 'vue';
	export default {
		data() {
			return {
				os_result: {},
				trem_res: [],
				student_id: '',
				exam_online: {},
				exam_local: {},
				exam_detail_show: {},
				exam_finished: {},
				exam_more: {},
				exam_detail_flag: false,
				exam_finished_flag: false,
				local_detail_show: {},
				local_finished: {},
				local_more: {},
				local_detail_flag: false,
				local_finished_flag: false,
				trem_show: [],
				trem_show_flag: false,
				this_trem_data: {},
				data_load_flag: false,
				colors: ['#ff0000', '#F37B1D', '#39B54A', '#3681BA', '#6739B6', '#000000']
			};
		},
		onLoad() {
			this.student_id = uni.getStorageSync('student_id');
			Vue.config.cookie = uni.getStorageSync('cookie');

			this.getOs_result(() => {
				this.os_result = Vue.config.os_result;
				this.getDatas(() => {
					this.getLocalMessage(this.os_result.semestercode);
					this.getTrems();
					this.getMessage(this.os_result.semestercode);
				}, () => {
					this.getLocalMessage(this.os_result.semestercode);
					this.getTrems();
					this.getMessage(this.os_result.semestercode);
				})
			});
		},
		onBackPress(event) {
			uni.switchTab({
				url: '../my/my'
			});
			return true;
		},
		onShow() {
			this.simpleCheck();
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			getDatas(funS, funF) {
				uni.showLoading({
					title: '加载中……'
				});
				uni.request({
					url: Vue.config.baseUrl[0] + 'datas',
					method: 'POST',
					withCredentials: true,
					header: {
						'content-type': 'application/x-www-form-urlencoded'
					},
					success: res => {
						uni.hideLoading();
						if (res.statusCode == 200) {
							this.this_trem_data = res.data.data[0];
							uni.setStorage({
								key: 'this_trem_data' + this.os_result.semestercode,
								data: this.this_trem_data
							});
							this.trem_res = [];
							let tem = res.data.data;
							for (let i = 0; i < tem.length; i++) {
								if (parseInt(this.student_id.substr(0, 4)) <= parseInt(tem[i].name.substr(0, 4))) {
									this.trem_res.push(tem[i]);
								}
							}
							uni.setStorage({
								key: 'allTrems',
								data: this.trem_res
							});
							if (typeof funS === "function") {
								funS();
							}
						} else {
							this.error.school();
							this.getDatas_local(funF);
						}
					},
					fail: res => {
						uni.hideLoading();
						this.error.internet();
						this.getDatas_local(funF);
					}
				});
			},
			getDatas_local(fun) {
				uni.getStorage({
					key: 'this_trem_data' + this.os_result.semestercode,
					success: (res) => {
						this.this_trem_data = res.data;
						uni.getStorage({
							key: 'allTrems',
							success: (res) => {
								this.trem_res = res.data;
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
					},
					fail: (res) => {
						uni.showModal({
							title: '错误',
							content: '未获取有效数据，请在网络连接正常、教务可以正常登录后重新尝试，或联系管理员。',
							showCancel: false,
							confirmText: '了解'
						});
					}
				});
			},
			getTrems() {
				if (this.trem_res[0].code < this.os_result.semestercode) {
					this.trem_res.unshift({
						code: this.os_result.semestercode,
						name: this.this_trem_data.name,
						season: this.this_trem_data.season,
						year: this.this_trem_data.year
					});
				}
				this.trem_show = [];
				for (var i = 0; i < this.trem_res.length; i++) {
					this.trem_show.push(true);
				}
				this.trem_show_flag = !this.trem_show_flag;
			},
			getMessage(code) {
				uni.showLoading({
					title: '加载中……',
					mask: true
				});
				uni.getStorage({
					key: 'exam_online' + this.student_id,
					success: res => {
						this.exam_online = res.data;
					},
					fail: res => {
						this.exam_online = {};
					},
					complete: res => {
						Vue.config.cookie = uni.getStorageSync('cookie');
						uni.request({
							url: Vue.config.baseUrl[0] + 'exam',
							method: 'POST',
							withCredentials: true,
							header: {
								'content-type': 'application/x-www-form-urlencoded',
								'cookie': Vue.config.cookie
							},
							data: {
								semestercode: code
							},
							success: res => {
								if (res.data.code == this.code.success) {
									this.exam_online[code] = res.data.data;
									uni.setStorage({
										key: 'exam_online' + this.student_id,
										data: this.exam_online
									});
									this.initial_online(code);
								} else if (res.data.code == this.code.unLogin) {
									uni.hideLoading();
									this.error.login();
								} else {
									this.error.school();
									if (this.exam_online[code] == null) {
										this.exam_online[code] = [];
									}
									uni.setStorage({
										key: 'exam_online' + this.student_id,
										data: this.exam_online
									});
									this.initial_online(code);
								}
							},
							fail: res => {
								this.error.internet();
								if (this.exam_online[code] == null) {
									this.exam_online[code] = [];
								}
								uni.setStorage({
									key: 'exam_online' + this.student_id,
									data: this.exam_online
								});
								this.initial_online(code);
							}
						});
					}
				});
			},
			getLocalMessage(code) {
				uni.getStorage({
					key: 'exam_local' + this.student_id,
					success: res => {
						this.exam_local = res.data;
						if (this.exam_local[code] == null) {
							this.exam_local[code] = [];
						}
						this.initial_local(code);
					},
					fail: res => {
						this.exam_local[code] = [];
					},
					complete: res => {
						uni.setStorage({
							key: 'exam_local' + this.student_id,
							data: this.exam_local
						});
					}
				});
			},
			initial_online(index) {
				uni.getStorage({
					key: 'exam_finished' + this.student_id,
					success: res => {
						this.exam_finished = res.data;
						if (this.exam_finished[index] == null) {
							this.exam_finished[index] = {};
						}
					},
					fail: res => {
						this.exam_finished[index] = {};
					},
					complete: res => {
						this.exam_detail_show[index] = [];
						for (var i = 0; i < this.exam_online[index].length; i++) {
							this.exam_detail_show[index].push(true);
							if (this.exam_finished[index][this.exam_online[index][i].lesson_code] == null) {
								this.exam_finished[index][this.exam_online[index][i].lesson_code] = this.exam_online[index][i].is_completed;
							}
						}
						this.exam_detail_flag = !this.exam_detail_flag;
						this.exam_finished_flag = !this.exam_finished_flag;

						uni.getStorage({
							key: 'exam_more' + this.student_id,
							success: res => {
								this.exam_more = res.data;
								if (this.exam_more[index] == null) {
									this.exam_more[index] = {};
								}
							},
							fail: res => {
								this.exam_more[index] = {};
							},
							complete: res => {
								for (var i = 0; i < this.exam_online[index].length; i++) {
									if (this.exam_more[index][this.exam_online[index][i].lesson_code] == null) {
										this.exam_more[index][this.exam_online[index][i].lesson_code] = '';
									}
								}
								uni.setStorage({
									key: 'exam_more' + this.student_id,
									data: this.exam_more
								});
								var that = this;
								setTimeout(function() {
									that.$forceUpdate();
								}, 1000);
							}
						});
					}
				});

				uni.hideLoading();
			},
			initial_local(index) {
				uni.getStorage({
					key: 'local_finished' + this.student_id,
					success: res => {
						this.local_finished = res.data;
					},
					fail: res => {
						this.local_finished[index] = [];
					},
					complete: res => {
						this.local_detail_show[index] = [];
						for (var i = 0; i < this.exam_local[index].length; i++) {
							this.local_detail_show[index].push(true);
							if (this.local_finished[index][i] == null) {
								this.local_finished[index].push(false);
							}
						}
						uni.setStorage({
							key: 'local_finished' + this.student_id,
							data: this.local_finished
						});
					}
				});
				this.exam_detail_flag = !this.exam_detail_flag;
				this.exam_finished_flag = !this.exam_finished_flag;

				uni.getStorage({
					key: 'local_more' + this.student_id,
					success: res => {
						this.local_more = res.data;
						if (this.local_more[index] == null) {
							this.local_more[index] = [];
						}
					},
					fail: res => {
						this.local_more[index] = [];
					},
					complete: res => {
						for (var i = 0; i < this.exam_local[index].length; i++) {
							if (this.local_more[index][i] == null) {
								this.local_more[index].push('');
							}
						}
						uni.setStorage({
							key: 'local_more' + this.student_id,
							data: this.local_more
						});
					}
				});
			},
			showDetail(index, i) {
				this.exam_detail_show[index][i] = !this.exam_detail_show[index][i];
				this.exam_detail_flag = !this.exam_detail_flag;
			},
			showDetailL(index, i) {
				this.local_detail_show[index][i] = !this.local_detail_show[index][i];
				this.local_detail_flag = !this.local_detail_flag;
			},
			makeDone(index, co) {
				if (co != -1) {
					uni.showModal({
						title: '确认',
						content: '确定修改该事件的完成状态？',
						showCancel: true,
						confirmText: '确定',
						cancelText: '点错了',
						success: res => {
							if (res.confirm) {
								this.exam_finished[index][co] = !this.exam_finished[index][co];
								this.exam_finished_flag = !this.exam_finished_flag;
								uni.getStorage({
									key: 'exam_finished' + this.student_id,
									success: (res) => {
										res.data[index][co] = this.exam_finished[index][co];
										uni.setStorage({
											key: 'exam_finished' + this.student_id,
											data: res.data
										});
									},
									fail: (res) => {
										let tem = {};
										tem[index] = {};
										tem[index][co] = this.exam_finished[index][co];
										uni.setStorage({
											key: 'exam_finished' + this.student_id,
											data: tem
										});
									}
								})
							}
						}
					});
				}
			},
			makeDoneL(index, i) {
				uni.showModal({
					title: '确认',
					content: '确定修改该事件的完成状态？',
					showCancel: true,
					confirmText: '确定',
					cancelText: '点错了',
					success: res => {
						if (res.confirm) {
							this.local_finished[index][i] = !this.local_finished[index][i];
							this.local_finished_flag = !this.local_finished_flag;
							uni.setStorage({
								key: 'local_finished' + this.student_id,
								data: this.local_finished
							});
							this.$forceUpdate();
						}
					}
				});
			},
			showEvent(index) {
				this.trem_show[index] = !this.trem_show[index];
				this.trem_show_flag = !this.trem_show_flag;
			},
			ask() {
				uni.showModal({
					title: '提示',
					content: '您可以点击“未做”或“已完成”按钮修改事件状态，点击“备注”查看事件详情；“待做”事件会在右上角显示可编辑图标，您可以自定义事件属性；点击屏幕下方“添加事件按钮”您可以自定义添加备忘录（只能向当前学期添加哦）。',
					showCancel: false,
					confirmText: '了解'
				});
			},
			loadMessage(code) {
				this.getMessage(code);
				this.getLocalMessage(code);
				if (!this.data_load_flag) {
					this.data_load_flag = true;
					var that = this;
					setTimeout(function() {
						that.loadMessage(code);
					}, 200);
				}
			},
			editEvent(mode, code, index, co) {
				if (co != -1) {
					if (mode == 0) {
						uni.navigateTo({
							url: '../addTest/addTest?mode=0&code=' + this.os_result.semestercode
						});
					} else if (mode == 1) {
						if (!this.exam_finished[code][co]) {
							uni.navigateTo({
								url: '../addTest/addTest?mode=1&code=' + code + '&index=' + index
							});
						}
					} else {
						if (!this.local_finished[code][index]) {
							uni.navigateTo({
								url: '../addTest/addTest?mode=2&code=' + code + '&index=' + index
							});
						}
					}
				}
			}
		},
		computed: {
			returnHeight() {
				return function(index, i, co) {
					if (this.exam_finished_flag || !this.exam_finished_flag)
						if (this.exam_detail_flag || !this.exam_detail_flag) {
							// console.log(this.exam_detail_show)
							// console.log(this.exam_detail_show[index][i])
							if (this.exam_finished[index] !== undefined && this.exam_finished[index][co]) {
								return 1;
							} else if (this.exam_detail_show[index] != undefined && !this.exam_detail_show[index][i]) {
								return 2;
							} else {
								return 3;
							}
						}
				};
			},
			returnHeightL() {
				return function(index, i) {
					if (this.local_finished_flag || !this.local_finished_flag)
						if (this.local_detail_flag || !this.local_detail_flag) {
							if (this.local_finished[index][i]) {
								return 1;
							} else if (this.exam_detail_show[index] != undefined && !this.local_detail_show[index][i]) {
								return 2;
							} else {
								return 3;
							}
						}
				};
			},
			returnTremShow() {
				return function(index) {
					if (this.trem_show_flag || !this.trem_show_flag) {
						return this.trem_show[index];
					}
				};
			}
		}
	};
</script>

<style>
	@import url('./test.css');
</style>
