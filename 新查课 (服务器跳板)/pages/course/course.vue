<template>
	<view id="class_container" :style="[{ height: windowHeight - statusBarHeight + 'px' }]">
		<view @click="goToRegister" id="canApply" v-if="applystatus == 0 || applystatus == 1">
			<image style="width: 100%;height: 100%;" mode="aspectFill" src="../../static/share.jpg"></image>
			<view id="closeApply" @click.stop="closeApply">×</view>
			<view id="applyMore">点击了解详情</view>
		</view>

		<view class="statusBar" :style="{ height: statusBarHeight + 'px' }"></view>
		<image id="bgimg" src="../../static/my/bag.png"></image>

		<view id="tableBox" :style="[{ marginTop: statusBarHeight + 'px' }, { height: windowHeight - statusBarHeight + 'px' }]"
		 @click="hideWeek()">
			<view id="tableTitle">
				<!-- #ifdef APP-PLUS || H5 -->
				<view class="showAllClass" style="left: 20upx;right: unset;" @click="makeSureWeekIndex">本周课程</view>
				<!-- #endif -->
				<!-- #ifdef MP-QQ || MP-WEIXIN -->
				<view class="showAllClass" style="position: absolute;left: 20upx;right: unset;justify-content: space-around;">
					<view @click="makeSureWeekIndex">本周</view>
					<view style="width: 3upx;height: 100%;background-color: #FFFFFF;"></view>
					<view @click="showAllClass">{{ weekAllFlag ? '一周' : '全部' }}</view>
				</view>
				<!-- #endif -->
				<view id="weekSearch">
					<view class="dateSide" @click.stop="changeWeek(-1)">
						<view id="lastWeek"></view>
					</view>
					<view id="date" @click.stop="changeWeek(0)">{{ !weekAllFlag ? '第' + week : '全部' }}周</view>
					<view class="dateSide" @click.stop="changeWeek(1)">
						<view id="nextWeek"></view>
					</view>
				</view>
				<!-- #ifdef APP-PLUS || H5 -->
				<view class="showAllClass" @click="showAllClass">{{ weekAllFlag ? '一周' : '全部' }}课程</view>
				<!-- #endif -->
				<view id="choseWeek" ref="choseWeek" :animation="animationWeek">
					<view class="choseWeekNumBox">
						<view class="choseWeekNum" v-for="(id, index) in [101, 102, 103, 104, 105]" :style="[{ 'background-color': week == index + 1 ? '#76d897' : '#FFFFFF' }]"
						 :key="id" @click.stop="choseDate(index + 1)">
							{{ index + 1 }}
						</view>
					</view>
					<view class="choseWeekNumBox">
						<view class="choseWeekNum" :style="[{ 'background-color': week - 5 == index + 1 ? '#76d897' : '#FFFFFF' }]" v-for="(id, index) in [201, 202, 203, 204, 205]"
						 :key="id" @click.stop="choseDate(index + 6)">
							{{ index + 6 }}
						</view>
					</view>
					<view class="choseWeekNumBox">
						<view class="choseWeekNum" :style="[{ 'background-color': week - 10 == index + 1 ? '#76d897' : '#FFFFFF' }]"
						 v-for="(id, index) in [301, 302, 303, 304, 305]" :key="id" @click.stop="choseDate(index + 11)">
							{{ index + 11 }}
						</view>
					</view>
					<view class="choseWeekNumBox">
						<view class="choseWeekNum" :style="[{ 'background-color': week - 15 == index + 1 ? '#76d897' : '#FFFFFF' }]"
						 v-for="(id, index) in [401, 402, 403, 404, 405]" :key="id" @click.stop="choseDate(index + 16)">
							{{ index + 16 }}
						</view>
					</view>
				</view>
			</view>
			<view id="classBox">
				<view id="classTimeBox" @click="showTimeDetail()">
					<view id="weekDayWord">今日周{{ weekDayNow }}</view>
					<view style="width: 100%;height: 90%;">
						<view class="classTimeDiv">
							<view>1</view>
							<view>2</view>
						</view>
						<view class="classTimeDiv">
							<view>3</view>
							<view>4</view>
						</view>
						<view class="classTimeDiv">
							<view>5</view>
							<view>6</view>
						</view>
						<view class="classTimeDiv">
							<view>7</view>
							<view>8</view>
						</view>
						<view class="classTimeDiv">
							<view>9</view>
							<view>10</view>
							<view>11</view>
						</view>
					</view>
					<view id="classTimeDetail" :animation="animationTime">
						<view style="width: 100%;height: 10%;"></view>
						<view style="width: 220upx;height: 90%;padding-left: 20upx;background-color: #f2f2f2;">
							<view class="classTimeDiv">
								<view>08:00-08:50</view>
								<view>09:00-09:50</view>
							</view>
							<view class="classTimeDiv">
								<view>10:10-11:00</view>
								<view>11:10-12:00</view>
							</view>
							<view class="classTimeDiv">
								<view>14:00-14:50</view>
								<view>15:00-15:50</view>
							</view>
							<view class="classTimeDiv">
								<view>16:00-16:50</view>
								<view>17:00-17:50</view>
							</view>
							<view class="classTimeDiv">
								<view>19:00-19:50</view>
								<view>20:00-20:50</view>
								<view>21:00-21:50</view>
							</view>
						</view>
					</view>
				</view>
				<view id="classColumn">
					<view id="pickerBox">
						<picker mode="selector" :range="trem_res" :range-key="'name'" :value="tremNowIndex" id="tremPicker" @change="changeTrem">
							<view id="thisTremMes">
								<view>{{ this_trem_data.name }}【{{ this_trem_data.season }}】</view>
								<view @click.stop="changeTrem0()">{{ tremNowIndex == 0 ? nowTime : '查看本学期' }}</view>
							</view>
							<view id="weekDayBox">
								<view class="weekDayCon" :style="[{ color: week == weekNow && weekDayNow == '一' ? '#58b54a' : '#7f7f7f' }]">
									周一
									<br />
									{{ getDateFromWeek(1) }}
								</view>
								<view class="weekDayCon" :style="[{ color: week == weekNow && weekDayNow == '二' ? '#58b54a' : '#7f7f7f' }]">
									周二
									<br />
									{{ getDateFromWeek(2) }}
								</view>
								<view class="weekDayCon" :style="[{ color: week == weekNow && weekDayNow == '三' ? '#58b54a' : '#7f7f7f' }]">
									周三
									<br />
									{{ getDateFromWeek(3) }}
								</view>
								<view class="weekDayCon" :style="[{ color: week == weekNow && weekDayNow == '四' ? '#58b54a' : '#7f7f7f' }]">
									周四
									<br />
									{{ getDateFromWeek(4) }}
								</view>
								<view class="weekDayCon" :style="[{ color: week == weekNow && weekDayNow == '五' ? '#58b54a' : '#7f7f7f' }]">
									周五
									<br />
									{{ getDateFromWeek(5) }}
								</view>
								<view class="weekDayCon" :style="[{ color: week == weekNow && weekDayNow == '六' ? '#58b54a' : '#7f7f7f' }]">
									周六
									<br />
									{{ getDateFromWeek(6) }}
								</view>
								<view class="weekDayCon" :style="[{ color: week == weekNow && weekDayNow == '日' ? '#58b54a' : '#7f7f7f' }]">
									周日
									<br />
									{{ getDateFromWeek(7) }}
								</view>
							</view>
						</picker>

						<wyb-noticeBar v-if="ahead.status == 1" id="notice" :text="ahead.msg" :show-close="true" :extend-more-area="true"
						 @showMore="copyQQ" />
					</view>
					<swiper id="classColumnSwiper" :indicator-dots="false" :autoplay="false" :circular="false" :current="week-1"
					 @change="swiperChange">
						<swiper-item class="classDiv" v-for="(week_swiper, weekI_swiper) in 20" :key="weekI_swiper">
							<view class="classTime" v-for="(weekDay, weekDayIndex) in [1, 2, 3, 4, 5, 6, 7]" :key="weekDay">
								<view class="classSection" v-for="(section, sectionIndex) in [1, 2, 3, 4, 5]" :key="section" @click="addCourse(this_trem_data.name, this_trem_data.code, week, weekDayIndex + 1, 2 * sectionIndex + 1)"
								 :style="[{ 'border-bottom': section == 2 || section == 4 ? '#d3ddd1 1upx dotted' : '' }]">
									<view class="each_class" v-for="(cl, index) in class_res[week_swiper]" :style="[{ 'background-color': color_distribute[cl.lesson_code].bg }, {'color': color_distribute[cl.lesson_code].fo }, { height: cl.end_unit == cl.start_unit ? '50%' : '100%' }]"
									 v-if="!weekAllFlag && cl.weekday == weekDay && (cl.start_unit == 2 * (section - 1) + 1 || cl.start_unit == 2 * (section - 1) + 2) && color_distribute[cl.lesson_code] != null"
									 :key="cl.activity_id" @click.stop="seeCourse(cl.lesson_code)">
										<view class="class_name">{{ cl.course_name }}</view>
										<view class="class_place" :style="[{ height: cl.end_unit == cl.start_unit ? '52%' : '30%' }]">{{ cl.rooms[0] ? cl.rooms[0].name : '无' }}</view>
									</view>
									<view class="each_class" v-for="(cl, index) in class_res_local" :style="[{ 'background-color': color_distribute[cl.classNumber].bg }, {'color': color_distribute[cl.classNumber].fo }, { height: cl.end_unit == cl.start_unit ? '50%' : '100%' }]"
									 v-if="
									(weekAllFlag || cl.activeWeekLocal[week]) &&
										cl.weekday == weekDay &&
										(cl.start_unit == 2 * (section - 1) + 1 || cl.start_unit == 2 * (section - 1) + 2)
								"
									 :key="cl.activity_id" @click.stop="seeCourseLocal(index, os_result.semestercode)">
										<view class="class_name">{{ cl.courseName }}</view>
										<view class="class_place" :style="[{ height: cl.end_unit == cl.start_unit ? '52%' : '30%' }]">{{ cl.rooms[0] ? cl.rooms[0].name : '无' }}</view>
									</view>
									<view class="each_class" v-for="(cl, index) in class_res_all" :style="[{ 'background-color': color_distribute[cl.lesson_code].bg }, {'color': color_distribute[cl.lesson_code].fo }, { height: cl.end_unit == cl.start_unit ? '50%' : '100%' }]"
									 v-if="weekAllFlag && cl.weekday == weekDay && (cl.start_unit == 2 * (section - 1) + 1 || cl.start_unit == 2 * (section - 1) + 2)"
									 :key="index" @click.stop="seeCourse(cl.lesson_code)">
										<view class="class_name">{{ cl.course_name }}</view>
										<view class="class_place" :style="[{ height: cl.end_unit == cl.start_unit ? '52%' : '30%' }]">{{ cl.rooms[0] ? cl.rooms[0].name : '无' }}</view>
									</view>
								</view>
							</view>
						</swiper-item>
					</swiper>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import Vue from 'vue';
	import wybNoticeBar from '../../components/wyb-noticeBar/wyb-noticeBar.vue'
	export default {
		data() {
			return {
				statusBarHeight: '',
				windowHeight: '',
				tabarHeight: 50,
				os_result: {},
				this_trem_data: {},
				trem_res: [],
				student_id: '',
				colors: [{
						'bg': '#fadbd9',
						'fo': '#e54d42'
					},
					{
						'bg': '#fef4d6',
						'fo': '#fbc208'
					},
					{
						'bg': '#e8f4d9',
						'fo': '#a9c63f'
					},
					{
						'bg': '#d2f1f0',
						'fo': '#1cbbb4'
					},
					{
						'bg': '#ebd4ef',
						'fo': '#9c26b0'
					},
					{
						'bg': '#ede1d9',
						'fo': '#a5673f'
					},
					{
						'bg': '#cacaca',
						'fo': '#fefefe'
					},
					{
						'bg': '#f9d7ea',
						'fo': '#e4399e'
					},
					{
						'bg': '#fde6d2',
						'fo': '#f37b1d'
					},
					{
						'bg': '#d7f0db',
						'fo': '#39b54a'
					},
					{
						'bg': '#cce6ff',
						'fo': '#0081ff'
					},
					{
						'bg': '#e1d7f0',
						'fo': '#6739b6'
					},
					{
						'bg': '#e8f5fe',
						'fo': '#85a1c3'
					},
					{
						'bg': '#e7ebed',
						'fo': '#8799a3'
					}
				],
				color_index: 0,
				color_distribute: {},
				nowTime: '',
				showWeekChoose: false,

				firstDay: 1,
				week: 1,
				weekAllFlag: false,
				weekNow: 1,
				weekDayNow: 0,

				class_res: {},
				class_res_all: [],
				class_res_local: [],

				timeInterval: null,
				animationWeek: {},
				animationTime: {},
				timeDetailShow: false,
				tremNowIndex: 0,

				touchStartData: {
					sx: 0,
					ex: 0,
					sy: 0,
					ey: 0
				},
				shouldRefresh: false,
				applystatus: -1,

				ahead: {
					status: 0,
					msg: [],
					start: 0,
					value: 0
				}
			};
		},
		onLoad() {
			// #ifndef APP-PLUS
			this.tabarHeight = 0;
			// #endif
			this.color_index = parseInt(Math.random() * this.colors.length);

			this.simpleCheck((id) => {
				this.student_id = Vue.config.student_id;
				this.getApply(id, (res) => {
					this.applystatus = res;
				});
			});

			setTimeout(() => {
				//获取状态栏高度，setTimeout后才能调用uni.
				uni.getSystemInfo({
					success: res => {
						this.statusBarHeight = res.statusBarHeight;
						this.windowHeight = res.windowHeight;
					}
				});
			}, 1);

			this.getOs_result(() => {
				this.os_result = Vue.config.os_result;
				if (Vue.config.os_result.ahead.status == 1) {
					this.ahead = Vue.config.os_result.ahead;
				}
				this.getDatas(() => {
					this.makeSureWeekIndex();
					this.getMessage_local(this.os_result.semestercode);
					this.getAllClass_local(this.os_result.semestercode);
					this.getAllClassLocal(this.os_result.semestercode);
				}, () => {
					this.makeSureWeekIndex();
					this.getMessage_local(this.os_result.semestercode);
					this.getAllClass_local(this.os_result.semestercode);
					this.getAllClassLocal(this.os_result.semestercode);
				})
			});
		},
		onPullDownRefresh() {
			this.getApply(this.student_id);

			this.getOs_result(() => {
				this.getDatas(() => {
					this.makeSureWeekIndex();
					this.getAllClassLocal(this.os_result.semestercode);
					this.getMessage_online(this.os_result.semestercode, 1);
					this.getAllClassOnline(this.os_result.semestercode);
				}, () => {
					this.makeSureWeekIndex();
					this.getAllClassLocal(this.os_result.semestercode);
					this.getMessage_local(this.os_result.semestercode);
					this.getAllClass_local(this.os_result.semestercode);
				});
			})
		},
		onHide() {
			clearInterval(this.timeInterval);
		},
		onShow() {
			clearInterval(this.timeInterval);
			this.timeInterval = setInterval(() => {
				this.nowTime = new Date(new Date().getTime() + 8 * 3600 * 1000)
					.toJSON()
					.substr(0, 19)
					.replace('T', ' ');
			}, 500);
			if (this.shouldRefresh) {
				this.shouldRefresh = false;
				this.getAllClassLocal(this.os_result.semestercode);
			}
			this.simpleCheck();
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			copyQQ() {
				uni.setClipboardData({
					data: this.ahead.start,
					success: () => {
						uni.showModal({
							title: '温馨提示',
							content: '服务QQ群号已经复制！',
							showCancel: false,
							confirmText: '我知道了'
						});
					},
					fail: (res) => {
						uni.showModal({
							title: '温馨提示',
							content: '请搜索QQ群：' + this.ahead.start,
							showCancel: false,
							confirmText: '我知道了'
						})
					}
				});
			},
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
							//this.getTrems();
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
			makeSureWeekIndex() {
				let temDate = new Date();
				let localDate = new Date(temDate.getFullYear() + '/' + (temDate.getMonth() + 1) + '/' + temDate.getDate());
				let onlineDate_e = new Date(this.this_trem_data.weeks[this.os_result.weekIndx - 1].end_on.replace(/-/g, '/'));
				this.firstDay = this.this_trem_data.weeks[this.os_result.weekIndx - 1].begin_on;
				this.weekDayNow = new Array('日', '一', '二', '三', '四', '五', '六')[localDate.getDay()];
				if (localDate - onlineDate_e <= 0) {
					this.week = this.os_result.weekIndx;
				} else {
					this.week = this.os_result.weekIndx + parseInt((Math.floor((localDate - onlineDate_e) / (24 * 3600 * 1000)) - 1) /
						7) + 1;
				}
				this.week = this.week + parseInt(this.ahead.value);
				if (this.week > 20) {
					this.week = 20;
					uni.showToast({
						title: '等待教务更新',
						icon: 'none'
					});
				}
				this.weekNow = this.week;
				this.weekAllFlag = false;
			},
			getMessage_local(trem) {
				uni.getStorage({
					key: 'class_res' + trem + this.student_id,
					success: res => {
						this.class_res = res.data;
						this.distributeColor();
					},
					fail: res => {
						this.getMessage_online(trem);
					}
				});
			},
			getMessage_online(trem) {
				uni.showLoading({
					title: "加载中……",
					mask: true
				});
				// #ifdef MP-QQ
				uni.showToast({
					title:"加载中……",
					icon:"loading",
					duration:1000
				})
				// #endif
				Vue.config.cookie = uni.getStorageSync('cookie');
				uni.request({
					url: Vue.config.baseUrl[0] + 'newschedule',
					method: 'POST',
					withCredentials: true,
					header: {
						'content-type': 'application/x-www-form-urlencoded',
						cookie: Vue.config.cookie
					},
					data: {
						semestercode: trem
					},
					success: res => {
						if (res.data.code == this.code.success) {
							this.class_res = res.data.data;
							uni.setStorage({
								key: 'class_res' + trem + this.student_id,
								data: this.class_res
							});
							this.distributeColor();
							uni.hideLoading();
						} else if (res.data.code == this.code.unLogin) {
							uni.hideLoading();
							this.error.login();
						} else {
							uni.hideLoading();
							this.error.server();
						}
					},
					fail: res => {
						uni.hideLoading();
						this.error.internet();
					}
				});
			},
			getAllClass_local(trem) {
				uni.getStorage({
					key: 'class_res_all' + trem + this.student_id,
					success: res => {
						this.class_res_all = res.data;
					},
					fail: res => {
						this.getAllClassOnline(trem);
					}
				});
			},
			getAllClassOnline(trem) {
				Vue.config.cookie = uni.getStorageSync('cookie');
				uni.request({
					url: Vue.config.baseUrl[0] + 'schedule',
					method: 'POST',
					withCredentials: true,
					header: {
						'content-type': 'application/x-www-form-urlencoded',
						cookie: Vue.config.cookie
					},
					data: {
						weekIndx: '',
						semestercode: trem
					},
					success: res => {
						if (res.data.code == this.code.success) {
							this.class_res_all = res.data.data;
							uni.setStorage({
								key: 'class_res_all' + trem + this.student_id,
								data: this.class_res_all
							});
						} else if (res.data.code == this.code.unLogin) {
							this.error.login();
						} else {
							this.error.school();
						}
					},
					fail: res => {
						this.error.internet();
					}
				});
			},
			getAllClassLocal(trem) {
				uni.getStorage({
					key: 'class_local' + trem + this.student_id,
					success: res => {
						for (let i = 0; i < res.data.length; i++) {
							res.data[i].activeWeekLocal = [
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false,
								false
							];
							let tem = res.data[i].activity_week.split(',');
							for (let j = 0; j < tem.length; j++) {
								res.data[i].activeWeekLocal[tem[j] - '0'] = true;
							}
						}
						this.class_res_local = res.data;
					},
					fail: res => {
						this.class_res_local = [];
					},
					complete: res => {
						this.distributeColorLocal();
					}
				});
			},
			hideWeek() {
				this.animationWeek = uni
					.createAnimation({
						duration: 500,
						timingFunction: 'ease'
					})
					.height(uni.upx2px(0))
					.step()
					.export();
			},
			changeWeek(type) {
				if (type == 0) {
					if (this.showWeekChoose) {
						this.showWeekChoose = false;
						this.hideWeek();
					} else {
						this.showWeekChoose = true;
						this.animationWeek = uni
							.createAnimation({
								duration: 500,
								timingFunction: 'ease'
							})
							.height(uni.upx2px(400))
							.step()
							.export();
					}
				} else {
					if (this.weekAllFlag == false) {
						this.week += type;
						if (this.week < 1) {
							this.week = 1;
						} else if (this.week > 20) {
							this.week = 20;
						}
					} else {
						this.week = this.week + type;
						this.weekAllFlag = false;
						if (this.week < 1) {
							this.week = 1;
						} else if (this.week > 20) {
							this.week = 20;
						}
					}
				}
			},
			choseDate(num) {
				this.week = num;
				this.weekAllFlag = false;
				setTimeout(() => {
					this.hideWeek();
				}, 200);
			},
			distributeColor() {
				for (let key in this.class_res) {
					for (let i = 0; i < this.class_res[key].length; i++) {
						if (this.color_distribute[this.class_res[key][i].lesson_code] == null) {
							this.color_distribute[this.class_res[key][i].lesson_code] = this.colors[this.color_index % this.colors.length];
							this.color_index++;
						}
					}
				}
				this.$forceUpdate();
				uni.stopPullDownRefresh();
			},
			distributeColorLocal() {
				for (let i = 0; i < this.class_res_local.length; i++) {
					if (this.color_distribute[this.class_res_local[i].classNumber] == null) {
						this.color_distribute[this.class_res_local[i].classNumber] = this.colors[this.color_index % this.colors.length];
						this.color_index++;
					}
				}
			},
			showAllClass() {
				// let tem = this.week;
				// this.week = this.weekAllFlag;
				// this.weekAllFlag = tem;
				this.weekAllFlag = !this.weekAllFlag;
			},
			seeCourseLocal(index, trem) {
				if (this.tremNowIndex == 0) {
					uni.navigateTo({
						url: '../classDetail/classDetail?type=1&index=' + index + '&trem=' + trem + '&id=' + this.student_id
					});
				} else {
					uni.showToast({
						title: '只能查询最新学期的课程！',
						icon: 'none'
					});
				}
			},
			seeCourse(co) {
				if (this.tremNowIndex == 0) {
					uni.showLoading({
						title: '查询中……'
					});
					uni.request({
						url: Vue.config.baseUrl[1] + 'courses?number=' + co,
						method: 'GET',
						success: res => {
							let mes = res.data.data;
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
						fail: res => {
							uni.showModal({
								title: '提示',
								content: '本功能暂不支持离线使用，请查看网络或确认教务是否闭网',
								showCancel: false,
								confirmText: '确认'
							});
						}
					});
				} else {
					uni.showToast({
						title: '只能查看最新学期的课程！',
						icon: 'none'
					});
				}
			},
			addCourse(trem, num, week, weekDay, section) {
				if (this.tremNowIndex == 0) {
					uni.navigateTo({
						url: '../addCourse/addCourse?trem=' + trem + '&num=' + num + '&week=' + week + '&weekDay=' + weekDay +
							'&section=' + section
					});
				} else {
					uni.showToast({
						title: '只能向最新学期添加课程！',
						icon: 'none'
					})
				}
			},
			closeApply() {
				this.applystatus = -1;
			},
			goToRegister() {
				this.getApply(this.student_id, () => {}, () => {
					uni.request({
						url: Vue.config.baseUrl[3] + 'applogin?username=' + this.student_id,
						method: 'GET',
						success: res => {
							if (res.data.code == this.code.success) {
								uni.setStorageSync('user_id' + this.student_id, res.data.data.id);
								uni.navigateTo({
									url: '../apply/apply'
								});
							}
						}
					});
				});
			},
			showTimeDetail() {
				if (this.timeDetailShow) {
					this.timeDetailShow = false;
					this.animationTime = uni
						.createAnimation({
							duration: 500,
							timingFunction: 'ease'
						})
						.width(uni.upx2px(0))
						.step()
						.export();
				} else {
					this.timeDetailShow = true;
					this.animationTime = uni
						.createAnimation({
							duration: 500,
							timingFunction: 'ease'
						})
						.width(uni.upx2px(1000))
						.step()
						.export();
				}
			},
			changeTrem0() {
				if (this.tremNowIndex != 0) {
					let e = {};
					e.target = {};
					e.target.value = 0;
					this.changeTrem(e);
				}
			},
			changeTrem(e) {
				this.tremNowIndex = e.target.value;
				this.this_trem_data = this.trem_res[this.tremNowIndex];
				this.class_res = {};
				this.class_res_all = [];
				this.class_res_local = [];
				this.color_distribute = {};
				this.$forceUpdate();
				this.getAllClassLocal(this.this_trem_data.code);
				this.getMessage_local(this.this_trem_data.code);
				this.getAllClass_local(this.this_trem_data.code);
			},
			swiperChange(e) {
				this.week = e.detail.current + '' - '0' + 1;
				this.weekAllFlag = false;
			}
		},
		computed: {
			getDateFromWeek() {
				return function(weekDay) {
					if (this.weekAllFlag) {
						return ''
					} else if (this.this_trem_data.weeks != null) {
						let reDay = new Date(this.this_trem_data.weeks[0].begin_on);
						reDay = new Date(reDay.getTime() + ((this.week) * 7 + (weekDay - 1)) * 24 * 3600 * 1000);
						return reDay.getMonth() + 1 + '-' + reDay.getDate();
					}
				};
			},
			isCanPutCourse() {
				return function(str) {
					if (this.week == 0) {
						return true;
					} else {
						let checkArr = str.split(',');
						for (let i = 0; i < checkArr.length; i++) {
							if (this.week == checkArr[i]) {
								return true;
							}
						}
						return false;
					}
				};
			},
			dayKey() {
				return function(week, sec) {
					return week * 10 + sec;
				};
			},
			chooseWeek() {
				return function(index, add) {
					return index + add;
				};
			}
		},
		components: {
			wybNoticeBar
		}
	};
</script>

<style>
	@import url('course.css');
</style>
