<template>
	<view style="border:rgba(255,255,255,0) 0.1px solid;">
		<view class="statusBar" :style="{ height: statusBarHeight + 'px' }"></view>
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view id="title" :style="{ 'margin-top': statusBarHeight + 'px' }">
			<view id="title_more" @click="showNavigation = !showNavigation">
				<view class="title_more_line"></view>
				<view class="title_more_line" :animation="animationMore1"></view>
				<view class="title_more_line" :animation="animationMore2"></view>
			</view>
			<view>NEWX &#8226 课程查询系统</view>
			<view id="title_more_con" :animation="animationMore3">
				<navigator url="../grade/grade">查成绩</navigator>
				<navigator url="../test/test">查考试</navigator>
				<navigator url="../classSave/classSave">看收藏</navigator>
				<view @click="goToRegister" v-if="applystatus == 0">去报名</view>
			</view>
		</view>
		<view id="search_box" :style="{ 'margin-top': statusBarHeight + 'px' }" :animation="animationTitle">
			<image id="search_img" mode="widthFix" src="../../static/xiaoxin.png"></image>
			<view id="search_word_box">
				<view id="search_tabbar">
					<view :class="[{ search_choose: type == 0 }, {search_unchoose:true}]" @click="type = 0">教室</view>
					<view :class="[{ search_choose: type == 1 }, {search_unchoose:true}]" @click="type = 1">老师</view>
					<view :class="[{ search_choose: type == 2 }, {search_unchoose:true}]" @click="type = 2">课名</view>
					<view :class="[{ search_choose: type == 3 }, {search_unchoose:true}]" @click="type = 3">时间</view>
					<view :class="[{ search_choose: type == 4 }, {search_unchoose:true}]" @click="type = 4">班级</view>
					<!-- <view :class="[{ search_choose: type == 5 }, {search_unchoose:true}]" @click="type = 5">空教室</view> -->
				</view>
				<swiper id="search_input_swiper" :indicator-dots="false" :autoplay="false" :circular="true" :current="type" @change="swiperChange">
					<swiper-item class="search_input">
						<view class="input_img_box">
							<image class="input_img" mode="widthFix" src="../../static/query/local.png"></image>
						</view>
						<input class="search_input_style" type="number" maxlength="3" v-model="build_code" placeholder="教室编号" />
						<radio class="search_radio_style" :checked="build_type == 1" @click="build_type = 1">敬亭</radio>
						<radio class="search_radio_style" style="margin-left: 10upx;" :checked="build_type == 2" @click="build_type = 2">新安</radio>
						<view class="search_submit" @click="goToQuire(0)">
							<image class="search_img" mode="widthFix" src="../../static/query/search.png"></image>
							<view class="search_button">查询</view>
						</view>
					</swiper-item>
					<swiper-item class="search_input">
						<view class="input_img_box">
							<image class="input_img" mode="widthFix" src="../../static/query/teacher.png"></image>
						</view>
						<input class="search_input_style" style="width: 400upx;" type="text" maxlength="10" placeholder="请输入教师姓名" v-model="teacher_name" />
						<view class="search_submit" @click="goToQuire(1)">
							<image class="search_img" mode="widthFix" src="../../static/query/search.png"></image>
							<view class="search_button">查询</view>
						</view>
					</swiper-item>
					<swiper-item class="search_input">
						<view class="input_img_box">
							<image class="input_img" mode="widthFix" src="../../static/query/class.png"></image>
						</view>
						<input class="search_input_style" style="width: 400upx;" type="text" maxlength="20" placeholder="请输入课程名或代码"
						 v-model="class_name" />
						<view class="search_submit" @click="goToQuire(2)">
							<image class="search_img" mode="widthFix" src="../../static/query/search.png"></image>
							<view class="search_button">查询</view>
						</view>
					</swiper-item>
					<swiper-item class="search_input">
						<view class="input_img_box">
							<image class="input_img" mode="widthFix" src="../../static/query/time.png"></image>
						</view>
						<picker class="search_picker_style" mode="multiSelector" :range="timeDataArray" :value="timeChooseArray" @change="bindTimeChange">
							<view class="search_word">第{{ timeChooseArray[0] + 1 }}周{{ timeDataArray[1][timeChooseArray[1]] }}，{{ timeDataArray[2][timeChooseArray[2]] }}</view>
						</picker>
						<view class="search_submit" @click="goToQuire(3)">
							<image class="search_img" mode="widthFix" src="../../static/query/search.png"></image>
							<view class="search_button">查询</view>
						</view>
					</swiper-item>
					<swiper-item class="search_input">
						<view class="input_img_box">
							<image class="input_img" mode="widthFix" src="../../static/query/time.png"></image>
						</view>
						<picker class="search_picker_style" mode="multiSelector" :range="timeDataArray" :value="timeChooseArray" @change="bindTimeChange">
							<view class="search_word">专业班级</view>
						</picker>
						<view class="search_submit" @click="goToQuire(4)">
							<image class="search_img" mode="widthFix" src="../../static/query/search.png"></image>
							<view class="search_button">查询</view>
						</view>
					</swiper-item>
					<!-- <swiper-item class="search_input">
						<view class="input_img_box">
							<image class="input_img" mode="widthFix" src="../../static/query/time.png"></image>
						</view>
						<picker class="search_picker_style" mode="multiSelector" :range="timeDataArray" :value="timeChooseArray" @change="bindTimeChange">
							<view class="search_word">空教室</view>
						</picker>
						<view class="search_submit" @click="goToQuire(3)">
							<image class="search_img" mode="widthFix" src="../../static/query/search.png"></image>
							<view class="search_button">查询</view>
						</view>
					</swiper-item> -->
				</swiper>
				<view id="advancedQuery" @click="changeDrawer(true)">高级选项</view>
			</view>
		</view>

		<uni-drawer ref="menuDrawer" id="menuDrawer" :mask="true" :maskClick="false" mode="right" :width="220" :visible="true">
			<view style="padding:30rpx;">
				
			</view>
			<view id="drawerBottm">
				<view class="drawerButton" style="color: #0FB045;" @click="goToQuire(-1)">查询</view>
				<view>|</view>
				<view class="drawerButton" @click="changeDrawer(false)">取消</view>
			</view>
		</uni-drawer>
		
		<view id="res_box" v-show="hasDone">
			<view id="split_line_box">
				<view class="split_line"></view>
				<view class="split_word">{{ quireShowWord }}</view>
				<view class="split_line"></view>
			</view>
			<view class="lesson_box animated bounceInUp" v-for="(lesson, i) in res" :key="i" @click="gotoDetail(lesson)">
				<!--  -->
				<view class="lesson_title">
					<view class="lesson_title_con ellipsis_div" style="text-align: left;">{{ lesson.courseName }}</view>
					<view class="lesson_title_con ellipsis_div" style="text-align: right;">教师:{{ lesson.teacher }}</view>
				</view>
				<view class="lesson_body">
					<view class="lesson_body_grade_box">
						<view class="lesson_body_grade_text" style="font-size: 30upx;color: #007aff;">学分</view>
						<view class="lesson_body_grade_text" style="font-size: 50upx;color: #007aff;">{{ lesson.grade }}</view>
					</view>
					<view class="lesson_body_describe">
						<view class="lesson_body_con ellipsis_div" style="margin-bottom: 20upx;">{{ lesson.class }}</view>
						<view class="lesson_body_con ellipsis_div">{{ lesson.courseType }}</view>
					</view>
					<view class="lesson_body_button">
						<view :style="[{ 'margin-bottom': '20upx' }, { 'font-size': lesson.flag ? '16px' : '' }, { color: lesson.flag ? '#39B54A' : '#848484' }]"
						 @click.stop="toSave(lesson)">
							{{ lesson.flag ? '已收藏' : '收藏' }}
						</view>
						<view style="color: #848484;">详情</view>
					</view>
				</view>
				<view class="lesson_foot">{{ lesson.courseTerm }}</view>
			</view>
		</view>
		<view id="bottom_mes" v-if="hasDone">{{ page * 10 >= count ? '没有更多数据了……' : '上拉刷新' }}</view>
	</view>
</template>

<script>
	import Vue from 'vue';
	import uniDrawer from "@/components/uni-drawer/uni-drawer.vue"
	export default {
		data() {
			return {
				statusBarHeight: '',
				os_result: {},
				student_id: '0000000000',
				type: 0,
				hasDone: false,
				showNavigation: false,
				lessonSave: {},

				quireShowWord: '',
				page: 1,
				build_type: 1, //敬亭1，新安2
				build_code: '', //教室编号
				teacher_name: '', //老师名
				class_name: '', //课程名
				time_string: [],
				timeDataArray: [
					[
						'第一周',
						'第二周',
						'第三周',
						'第四周',
						'第五周',
						'第六周',
						'第七周',
						'第八周',
						'第九周',
						'第十周',
						'第十一周',
						'第十二周',
						'第十三周',
						'第十四周',
						'第十五周',
						'第十六周',
						'第十七周',
						'第十八周',
						'第十九周',
						'第二十周'
					],
					['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'],
					['第1~2节', '第3~4节', '第5~6节', '第7~8节', '第9~11节']
				],
				timeChooseArray: [0, 1, 0],
				temArray: ['0102', '0304', '0506', '0708', '0911'],

				res: [],
				count: -1,

				animationTitle: {},
				animationLesson: {},
				animationMore1: {},
				animationMore2: {},
				animationMore3: {},

				canReachBottom: true,
				applystatus: -1,
				touchStartData: {
					sx: 0,
					ex: 0,
					sy: 0,
					ey: 0
				}
			};
		},
		onLoad() {
			this.animation = uni.createAnimation();

			let _t = this;
			setTimeout(() => {
				//获取状态栏高度，setTimeout后才能调用uni.
				uni.getSystemInfo({
					success: function(res) {
						_t.statusBarHeight = res.statusBarHeight;
					}
				});
			}, 1);
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
			uni.request({
				url: Vue.config.baseUrl[0] + 'now',
				method: 'POST',
				withCredentials: true,
				header: {
					'content-type': 'application/x-www-form-urlencoded'
				},
				success: res => {
					if (res.data.code == this.code.success) {
						this.os_result = res.data;
						this.week_order = this.os_result.weekIndx;
						uni.setStorage({
							key: 'os_result',
							data: res.data
						});
					} else {
						uni.getStorage({
							key: 'os_result',
							success: res => {
								this.os_result = res.data;
							}
						});
					}
				},
				fail: res => {
					uni.getStorage({
						key: 'os_result',
						success: res => {
							this.os_result = res.data;
						}
					});
				}
			});
			this.animation2 = uni.createAnimation();
		},
		onShow() {
			uni.getStorage({
				key: 'student_id',
				success: res => {
					this.student_id = res.data;
				},
				complete: res => {
					uni.getStorage({
						key: 'lessonSave' + this.student_id,
						success: res => {
							this.lessonSave = res.data;
						},
						fail: res => {
							this.lessonSave = {};
						},
						complete: res => {
							this.checkSave();
							this.$forceUpdate();
						}
					});
				}
			});
		},
		onHide() {
			this.canReachBottom = true;
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			changeDrawer(show) {
				if (show) {
					this.$refs.menuDrawer.open();
				} else {
					this.$refs.menuDrawer.close();
				}
			},
			animationTitleRun() {
				if (!this.hasDone) {
					this.animation.translateY(0).step({
						duration: 400,
						timingFunction: 'ease'
					});
					this.animationTitle = this.animation.export();
					this.hasDone = true;
				}
			},
			goToQuire(type) {
				this.animation2
					.translateY(100)
					.opacity(0)
					.step({
						duration: 100,
						timingFunction: 'ease'
					});
				this.animationTitle = this.animation.export();

				setTimeout(() => {
					this.quireIndexFun(type, true);
				}, 100);
			},
			quireIndexFun(type, isNew) {
				if (type == -1) {
					if (this.build_code.length < 3 && this.teacher_name == '' && this.class_name == '' && this.time_string.length == 0) {
						uni.showToast({
							title: '请至少输入一条有效查找限制',
							icon: 'none'
						});
					}
				} else if (type == 0) {
					if (this.build_code.length < 3) {
						uni.showToast({
							title: '请正确填写教室编号，例如：101',
							icon: 'none'
						});
					} else {
						if (isNew) {
							this.page = 1;
							this.res = [];
						}
						this.quireClassRoom();
						this.animationTitleRun();

						let classRoom = '敬亭';
						if (this.build_type == 2) {
							classRoom = '新安';
						}
						this.quireShowWord = '查询教室：' + classRoom + this.build_code;
					}
				} else if (type == 1) {
					if (this.teacher_name == '') {
						uni.showToast({
							title: '请填写教师姓名',
							icon: 'none'
						});
					} else {
						if (isNew) {
							this.page = 1;
							this.res = [];
						}
						this.quireTeacher();
						this.animationTitleRun();

						this.quireShowWord = '查询教师：' + this.teacher_name;
					}
				} else if (type == 2) {
					if (this.class_name == '') {
						uni.showToast({
							title: '请填写课程名或课程代码，例如：高数',
							icon: 'none'
						});
					} else {
						if (isNew) {
							this.page = 1;
							this.res = [];
						}
						this.quireLesson();
						this.animationTitleRun();

						this.quireShowWord = '查询课程：' + this.class_name;
					}
				} else if (type == 3) {
					if (isNew) {
						this.page = 1;
						this.res = [];
					}
					this.quireTime();
					this.animationTitleRun();

					this.quireShowWord =
						'查询时间：第' + (this.timeChooseArray[0] + 1) + '周' + this.timeDataArray[1][this.timeChooseArray[1]] + '，' + this.timeDataArray[
							2][this.timeChooseArray[2]];
				}
			},
			quireClassRoom() {
				uni.showLoading({
					title: '查询中……'
				});
				uni.request({
					url: Vue.config.baseUrl[1] + 'classroom/index/classroom/?classroom=' + this.build_type + this.build_code +
						'&page=' + this.page,
					method: 'GET',
					success: res => {
						if (res.data.data.length == 0) {
							uni.hideLoading();
							uni.showToast({
								title: '没有查到更多数据哦',
								icon: 'none'
							});
							this.count = 0;
						} else {
							uni.hideLoading();
							this.res = this.res.concat(res.data.data);
							this.checkSave();
							this.count = res.data.count;
						}
					},
					fail: res => {
						uni.hideLoading();
						this.error.internet();
					},
					complete: res => {
						this.animation2
							.translateY(0)
							.opacity(1)
							.step({
								duration: 400,
								timingFunction: 'ease',
								delay: 100
							});
						this.animationLesson = this.animation2.export();
						setTimeout(() => {
							this.canReachBottom = true;
						}, 200);
					}
				});
			},
			quireTeacher() {
				uni.showLoading({
					title: '查询中……'
				});
				uni.request({
					url: Vue.config.baseUrl[1] + 'teacher/index/teacher/?teacher=' + this.teacher_name + '&page=' + this.page,
					method: 'GET',
					success: res => {
						if (res.data.data.length == 0) {
							uni.hideLoading();
							uni.showToast({
								title: '没有查到更多数据哦',
								icon: 'none'
							});
							this.count = 0;
						} else {
							uni.hideLoading();
							this.res = this.res.concat(res.data.data);
							this.checkSave();
							this.count = res.data.count;
						}
					},
					fail: res => {
						uni.hideLoading();
						this.error.internet();
					},
					complete: res => {
						this.animation2
							.translateY(0)
							.opacity(1)
							.step({
								duration: 400,
								timingFunction: 'ease',
								delay: 100
							});
						this.animationLesson = this.animation2.export();
						setTimeout(() => {
							this.canReachBottom = true;
						}, 200);
					}
				});
			},
			quireLesson() {
				uni.showLoading({
					title: '查询中……'
				});
				uni.request({
					url: Vue.config.baseUrl[1] + 'lesson/index/lesson/?lesson=' + this.class_name + '&page=' + this.page,
					method: 'GET',
					success: res => {
						if (res.data.data.length == 0) {
							uni.hideLoading();
							uni.showToast({
								title: '没有查到更多数据哦',
								icon: 'none'
							});
							this.count = 0;
						} else {
							uni.hideLoading();
							this.res = this.res.concat(res.data.data);
							this.checkSave();
							this.count = res.data.count;
						}
					},
					fail: res => {
						uni.hideLoading();
						this.error.internet();
					},
					complete: res => {
						this.animation2
							.translateY(0)
							.opacity(1)
							.step({
								duration: 400,
								timingFunction: 'ease',
								delay: 100
							});
						this.animationLesson = this.animation2.export();
						setTimeout(() => {
							this.canReachBottom = true;
						}, 200);
					}
				});
			},
			quireTime() {
				uni.showLoading({
					title: '查询中……'
				});
				//console.log(Vue.config.baseUrl[1] + 'time/index/time/?week='+(this.timeChooseArray[0]+1)+'&class='+(((this.timeChooseArray[1]+6)%7+1)*10000+(this.timeChooseArray[2]+1)*100+this.timeChooseArray[3]+2))
				uni.request({
					url: Vue.config.baseUrl[1] +
						'time/index/time/?week=' +
						(this.timeChooseArray[0] + 1) +
						'&class=' +
						(((this.timeChooseArray[1] + 6) % 7) + 1) +
						this.temArray[this.timeChooseArray[2]] +
						'&page=' +
						this.page,
					method: 'GET',
					success: res => {
						if (res.data.data.length == 0) {
							uni.hideLoading();
							uni.showToast({
								title: '没有查到更多数据哦',
								icon: 'none'
							});
							this.count = 0;
						} else {
							uni.hideLoading();
							this.res = this.res.concat(res.data.data);
							this.checkSave();
							this.count = res.data.count;
						}
					},
					fail: res => {
						uni.hideLoading();
						this.error.internet();
					},
					complete: res => {
						this.animation2
							.translateY(0)
							.opacity(1)
							.step({
								duration: 400,
								timingFunction: 'ease',
								delay: 100
							});
						this.animationLesson = this.animation2.export();
						setTimeout(() => {
							this.canReachBottom = true;
						}, 200);
					}
				});
			},
			checkSave() {
				for (let i = 0; i < this.res.length; i++) {
					if (this.lessonSave[this.res[i].classNumber]) {
						this.res[i].flag = true;
					} else {
						this.res[i].flag = false;
					}
				}
			},
			bindTimeChange(e) {
				this.timeChooseArray = e.target.value;
			},
			swiperChange(e) {
				this.type = e.detail.current;
			},
			gotoDetail(mes) {
				uni.showLoading({
					title: '查询中……'
				});
				uni.setStorage({
					key: 'lessonToSee',
					data: mes,
					success: res => {
						uni.hideLoading();
						uni.navigateTo({
							url: '../classDetail/classDetail'
						});
					},
					fail: res => {
						uni.hideLoading();
						uni.showModal({
							title: '程序异常',
							showCancel: false,
							confirmText: '确认'
						});
					}
				});
			},
			toSave(lesson) {
				if (lesson.flag != true) {
					uni.showLoading({
						title: '保存中……'
					});
					this.lessonSave[lesson.classNumber] = lesson;
					uni.setStorage({
						key: 'lessonSave' + this.student_id,
						data: this.lessonSave,
						success: res => {
							uni.hideLoading();
							uni.showToast({
								title: '保存成功！',
								duration: 2000
							});
							lesson.flag = true;
							this.$forceUpdate();
						},
						fail: res => {
							uni.hideLoading();
							uni.showToast({
								title: '保存失败',
								icon:'none',
								duration: 2000
							});
						}
					});
				} else {
					uni.showModal({
						title: '请确认',
						content: '确定要删除该收藏课程？删除后将失去关于该课程的备注信息。',
						showCancel: true,
						cancelText: '点错了',
						confirmText: '确定',
						success: res => {
							if (res.confirm) {
								uni.showLoading({
									title: '正在删除……',
									mask: true
								});
								delete this.lessonSave[lesson.classNumber];
								uni.setStorage({
									key: 'lessonSave' + this.student_id,
									data: this.lessonSave,
									success: res => {
										uni.hideLoading();
										uni.showToast({
											title: '删除成功！',
											duration: 1000,
											mask: true
										});
										lesson.flag = false;
										this.$forceUpdate();
									},
									fail: res => {
										uni.hideLoading();
										uni.showToast({
											title: '删除失败',
											icon:'none',
											duration: 1000
										});
									}
								});
							}
						}
					});
				}
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
					success: (res) => {
						uni.hideLoading();
						if (res.data.status == 0) {
							uni.request({
								url: Vue.config.baseUrl[3] + "applogin?username=" + this.student_id,
								method: 'GET',
								success: (res) => {
									if (res.data.code == this.code.success) {
										uni.setStorageSync("user_id" + this.student_id, res.data.data.id);
										uni.navigateTo({
											url: '../apply/apply'
										});
									}
								}
							})
						} else {
							uni.showModal({
								title: '提示',
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
							content: '请检查网络连接',
							showCancel: false,
							confirmText: '了解'
						});
					}
				});
			}
		},
		onReachBottom() {
			if (this.canReachBottom) {
				this.canReachBottom = false;
				if (this.page * 10 < this.count) {
					this.page++;
					this.quireIndexFun(this.type, false);
				}
			}
		},
		components: {
			uniDrawer
		},
		watch: {
			showNavigation: function(newVal, oldVal) {
				let animation_more_1 = uni.createAnimation();
				let animation_more_2 = uni.createAnimation();
				let animation_more_3 = uni.createAnimation();
				if (newVal) {
					animation_more_1.rotate(20).step({
						duration: 400,
						transformOrigin: '0 0 0',
						timingFunction: 'ease'
					});
					animation_more_2.rotate(-20).step({
						duration: 400,
						transformOrigin: '0 0 0',
						timingFunction: 'ease'
					});
					animation_more_3.height(40).step({
						duration: 400,
						timingFunction: 'ease'
					});
					this.animationMore1 = animation_more_1.export();
					this.animationMore2 = animation_more_2.export();
					this.animationMore3 = animation_more_3.export();
				} else {
					animation_more_1.rotate(0).step({
						duration: 400,
						transformOrigin: '0 0 0',
						timingFunction: 'ease'
					});
					animation_more_2.rotate(0).step({
						duration: 400,
						transformOrigin: '0 0 0',
						timingFunction: 'ease'
					});
					animation_more_3.height(0).step({
						duration: 400,
						timingFunction: 'ease'
					});
					this.animationMore1 = animation_more_1.export();
					this.animationMore2 = animation_more_2.export();
					this.animationMore3 = animation_more_3.export();
				}
			}
		}
	};
</script>

<style>
	@import url('./query.css');
	@import url("../overall/animate.css");
</style>
