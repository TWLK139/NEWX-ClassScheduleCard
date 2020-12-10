<template>
	<view>
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view id="box">
			<view class="editBox">
				<view class="editName">课程名称：</view>
				<input class="editEdit" maxlength="20" v-model="course.courseName" placeholder="新建课程"></input>
			</view>
			<view class="editBox">
				<view class="editName">课程描述：</view>
				<input class="editEdit" maxlength="20" v-model="course.courseNumber" placeholder="每周班会"></input>
			</view>
			<view class="editBox">
				<view class="editName">班级：</view>
				<input class="editEdit" maxlength="100" v-model="course.class" placeholder="我的班级"></input>
			</view>
			<view class="editBox">
				<view class="editName">班级代码：</view>
				<input class="editEdit" maxlength="10" :value="course.classNumber" :disabled="true"></input>
			</view>
			<view class="editBox">
				<view class="editName samll_editName">学分：</view>
				<input class="editEdit samll_editEdit" maxlength="4" v-model="course.grade" placeholder="0"></input>
				<view class="editName samll_editName" style="border-left: #CCCCCC 2upx solid;padding-left: 25upx;">考核：</view>
				<input class="editEdit samll_editEdit" maxlength="4" v-model="course.method" placeholder="无考核"></input>
			</view>
			<view class="editBox">
				<view class="editName">教师：</view>
				<input class="editEdit" maxlength="100" v-model="course.teacher" placeholder="主持人"></input>
			</view>
			<view class="editBox">
				<view class="editName">教师等级：</view>
				<input class="editEdit" maxlength="100" v-model="course.teacherLevel" placeholder="辅导员"></input>
			</view>
			<view class="editBox">
				<view class="editName">开课周：</view>
				<picker mode="selector" :range="weekTypeWord" :value="weekType" @change="weekTypeChange">
					<view class="editEdit samll_editEdit" style="width: 98upx;font-size: 30upx;">{{ weekTypeWord[weekType] }}</view>
				</picker>

				<picker mode="selector" :range="[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]" :value="week_s" @change="chooseWeek_s">
					<view class="editEdit samll_editEdit" style="width: 98upx;font-size: 30upx;">第{{week_s+''-'0'+1}}周</view>
				</picker>
				<view class="lineTo"></view>
				<picker mode="selector" :range="[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]" :value="week_e" @change="chooseWeek_e">
					<view class="editEdit samll_editEdit" style="width: 98upx;font-size: 30upx;">第{{week_e+''-'0'+1}}周</view>
				</picker>
			</view>
			<view class="editBox">
				<view class="editName samll_editName">星期：</view>
				<picker mode="selector" :range="[1,2,3,4,5,6,7]" :value="weekDay" @change="chooseWeekDay">
					<view class="editEdit samll_editEdit" style="width: 35upx;">{{ weekDay+''-'0'+1 }}</view>
				</picker>
				<view class="editName samll_editName" style="border-left: #CCCCCC 2upx solid;padding-left: 25upx;">节：</view>
				<picker mode="selector" :range="[1,2,3,4,5,6,7,8,9,10,11]" :value="section_s" @change="chooseSection_s">
					<view class="editEdit samll_editEdit" style="width: 98upx;font-size: 30upx;">第{{section_s+''-'0'+1}}节</view>
				</picker>
				<view class="lineTo"></view>
				<picker mode="selector" :range="[1,2,3,4,5,6,7,8,9,10,11]" :value="section_e" @change="chooseSection_e">
					<view class="editEdit samll_editEdit" style="width: 98upx;font-size: 30upx;">第{{section_e+''-'0'+1}}节</view>
				</picker>
			</view>
			<view class="editBox">
				<view class="editName">课程类型：</view>
				<input class="editEdit" maxlength="10" v-model="course.courseType" placeholder="自定义课程"></input>
			</view>
			<view class="editBox">
				<view class="editName">开课学期：</view>
				<input class="editEdit" maxlength="10" :value="course.courseTerm" :disabled="true"></input>
			</view>

			<view class="editBox">
				<view class="editName samll_editName">地点：</view>
				<picker mode="selector" :range="course_place_word" :value="course_place" @change="chooseCoursePlace">
					<view class="editEdit samll_editEdit">{{course_place_word[course_place]}}</view>
				</picker>
				<view class="editName samll_editName" style="border-left: #CCCCCC 2upx solid;padding-left: 25upx;">{{(course_place==0||course_place==8||course_place==9)?"描述：":"号码："}}</view>
				<input class="editEdit samll_editEdit" v-model="course_place_num" placeholder="101"></input>
			</view>
			<view class="editBox">
				<view class="editName">备注：</view>
				<textarea class="editEdit_arer" maxlength="200" v-model="course.remarks" placeholder="事件备注"></textarea>
			</view>
			<view class="editBox" style="flex-wrap: nowrap;border-bottom: none;">
				<view class="saveButton" style="background-color: #3681BA;" @click="saveButton()">保存</view>
				<view class="saveButton" style="width: 10%;"></view>
				<view class="saveButton" style="background-color: #8d8d8d;" @click="deleteButton()">取消</view>
			</view>
		</view>
		<view style="width: 100%;height: 100upx;"></view>
	</view>
</template>

<script>
	import Vue from 'vue';
	export default {
		data() {
			return {
				student_id: '',
				course: {
					courseName: '',
					courseType: '',
					courseTerm: '',
					method: '',
					class: '',
					teacher: '',
					teacherLevel: '',
					classNumber: '',
					courseNumber: '',
					grade: 0,
					timePlace: [{
						week: 0,
						lesson: 0,
						type: 0,
						place: 0,
						other: ''
					}],
					weekday: 0,
					rooms: [{
						name: ''
					}],
					remarks: '',
					activity_week: '',
					end_unit: 0,
					start_unit: 0
				},
				weekType: 0,
				weekTypeWord: ['单双周', '单周', '双周'],
				week_s: 0,
				week_e: 1,
				course_place: 1,
				course_place_word: ['其他', '敬亭学堂', '新安学堂', '计算机楼', '综合楼一', '综合楼二', '工训中心', '化工楼', '风雨操场', '体育馆'],
				course_place_num: '',
				trem_code: '',
				weekDay: 1,
				section_s: 1,
				section_e: 2,
				class_local: [],

				type: 0,
				index: 0
			}
		},
		onLoad(option) {

			uni.showLoading({
				title: '加载中……'
			});
			// type == 1表示当前为修改功能，修改从课程详情页面跳转过来
			if (option.type == 1) {
				this.type = option.type;
				this.student_id = option.id;
				this.trem_code = option.num;
				this.index = option.index;
				this.student_id = uni.getStorageSync('student_id')
				uni.getStorage({
					key: 'class_local' + this.trem_code + this.student_id,
					success: (res) => {
						uni.hideLoading();
						this.class_local = res.data;
						if (this.class_local[this.index] != null) {
							this.course = this.class_local[this.index];

							this.trem_code = option.num;
							this.week_s = this.course.activity_week.substr(0, 1) + '' - '0' - 1;
							this.week_e = this.course.activity_week.substr(this.course.activity_week.length + '' - '0' - 1, 1) + '' - '0' -
								1;
							this.section_s = this.course.start_unit + '' - '0' - 1;
							this.section_e = this.course.end_unit + '' - '0' - 1;
							this.weekDay = this.course.weekday + '' - '0' - 1;
							this.course_place = parseInt((this.course.timePlace[0].place + '' - '0') / 1000);
							this.course_place_num = (this.course.timePlace[0].place + '' - '0') % 1000;
						} else {
							uni.showToast({
								title: '课程不存在',
								duration: 1000
							});
							setTimeout(() => {
								uni.navigateBack();
							}, 1000);
						}
					},
					fail: (res) => {
						uni.hideLoading();
						uni.showToast({
							title: '课程不存在',
							duration: 1000
						});
						setTimeout(() => {
							uni.navigateBack();
						}, 1000);
					}
				});
			} else {
				this.trem_code = option.num;
				this.course.courseTerm = option.trem;
				this.week_s = option.week + '' - '0' - 1;
				this.week_e = option.week + '' - '0' - 1;
				this.section_s = option.section + '' - '0' - 1;
				this.section_e = this.section_s + '' - '0' + 1;
				this.weekDay = option.weekDay + '' - '0' - 1;
				this.student_id = uni.getStorageSync('student_id');
				uni.getStorage({
					key: 'class_local' + this.trem_code + this.student_id,
					success: (res) => {
						this.class_local = res.data;
					},
					fail: (res) => {
						this.class_local = [];
					},
					complete: (res) => {
						uni.hideLoading();
						this.course.classNumber = (new Date()).getTime();
					}
				});
			}
		},
		onShow() {
			this.simpleCheck();
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			weekTypeChange(e) {
				this.weekType = e.target.value + '' - '0';
			},
			chooseWeek_s(e) {
				this.week_s = e.target.value + '' - '0';
				if (this.weekType + '' - '0' == 1 && (this.week_s + '' - '0') % 2 == 1) {
					this.week_s = this.week_s + '' - '0' - 1;
				} else if (this.weekType + '' - '0' == 2 && (this.week_s + '' - '0') % 2 == 0) {
					this.week_s = this.week_s + '' - '0' - 1;
					if (this.week_s + '' - '0' < 0) {
						this.week_s = 1;
					}
				}
			},
			chooseWeek_e(e) {
				this.week_e = e.target.value + '' - '0';
				if (this.weekType + '' - '0' == 1 && (this.week_e + '' - '0') % 2 == 1) {
					// console.log(this.week_e)
					this.week_e = this.week_e + '' - '0' + 1;
					// console.log(this.week_e)
					if (this.week_e + '' - '0' >= 20) {
						this.week_e = 18;
					}
				} else if (this.weekType + '' - '0' == 2 && (this.week_e + '' - '0') % 2 == 0) {
					this.week_e = this.week_e + '' - '0' + 1;
				}
			},
			chooseWeekDay(e) {
				this.weekDay = e.target.value + '' - '0';
			},
			chooseSection_s(e) {
				this.section_s = e.target.value + '' - '0';
				if (this.section_e < this.section_s) {
					this.section_e = this.section_s + '' - '0';
				}
				if (this.section_s + '' - '0' < 8) {
					if ((this.section_s + '' - '0') % 2 == 1) {
						this.section_e = this.section_s + '' - '0';
					} else {
						this.section_e = this.section_s + '' - '0' + 1;
					}
				}
			},
			chooseSection_e(e) {
				this.section_e = e.target.value;
				if (this.section_e < this.section_s) {
					this.section_s = this.section_e + '' - '0';
				}
				if (this.section_s + '' - '0' < 8) {
					if ((this.section_e + '' - '0') % 2 == 0) {
						this.section_s = this.section_e + '' - '0';
					} else {
						this.section_s = this.section_e + '' - '0' - 1;
					}
				}
			},
			chooseCoursePlace(e) {
				this.course_place = e.target.value;
			},
			saveButton() {
				uni.showLoading({
					title: '保存中……'
				});
				this.checkData();
				this.course.timePlace[0].week = (this.week_s + '' - '0' + 1) * 100 + (this.week_e + '' - '0' + 1);
				this.course.timePlace[0].lesson = (this.weekDay + '' - '0' + 1) * 10000 + (this.section_s + '' - '0' + 1) * 100 + (
					this.section_e + '' - '0' + 1);
				this.course.timePlace[0].type = this.weekType;
				this.course.timePlace[0].place = (this.course_place + '' - '0') * 1000;
				if (this.course_place + '' - '0' == 0 || this.course_place + '' - '0' == 8 || this.course_place + '' - '0' == 9) {
					this.course.timePlace[0].other = this.course_place_num;
					this.course.timePlace[0].place += 1;
				} else {
					this.course.timePlace[0].place += this.course_place_num;
				}

				let step = 1;
				if (this.weekType != 0) {
					step = 2;
				}
				this.course.activity_week = "";
				for (let i = this.week_s + '' - '0'; i <= this.week_e + '' - '0'; i = i + step) {
					this.course.activity_week += ((i + 1) + ',')
				}
				this.course.activity_week = this.course.activity_week.substr(0, this.course.activity_week.length + '' - '0' - 1);
				this.course.start_unit = this.section_s + '' - '0' + 1;
				this.course.end_unit = this.section_e + '' - '0' + 1;
				if (this.course_place == 0) {
					this.course.rooms[0].name = this.course_place_num;
				} else {
					this.course.rooms[0].name = this.course_place_word[this.course_place] + this.course_place_num;
				}
				this.course.weekday = this.weekDay + '' - '0' + 1;

				if (this.type == 1) {
					this.class_local[this.index] = this.course;
				} else {
					this.class_local.push(this.course);
				}
				uni.setStorage({
					key: 'class_local' + this.trem_code + this.student_id,
					data: this.class_local,
					success: (res) => {
						uni.showModal({
							title: '成功',
							content: '保存成功！',
							showCancel: false,
							success: (res) => {
								let pages = getCurrentPages();
								let prevPage = pages[pages.length - 2];
								prevPage.$vm.shouldRefresh = true;
								uni.navigateBack();
							},
							complete: (res) => {
								uni.hideLoading();
							}
						})
					},
					fail: (res) => {
						uni.hideLoading();
						uni.showModal({
							title: '失败',
							content: '保存失败',
							showCancel: false,
						})
					}
				})
			},
			checkData() {
				if (this.course.class == '') {
					this.course.class = '我的班级';
				}
				if (this.course.courseName == '') {
					this.course.courseName = '新建课程';
				}
				if (this.course.courseNumber == '') {
					this.course.courseNumber = '每周班会';
				}
				if (this.course.courseType == '') {
					this.course.courseType = '自定义课程';
				}
				if (this.course.grade == '') {
					this.course.grade = 0;
				}
				if (this.course.method == '') {
					this.course.method = '无考核';
				}
				if (this.course.teacher == '') {
					this.course.teacher = '主持人';
				}
				if (this.course.teacherLevel == '') {
					this.course.teacherLevel = '辅导员';
				}
				if (this.course_place_num == '') {
					this.course_place_num = 101;
				}
				if (this.course.remarks == '') {
					this.course.remarks = '无'
				}
			},
			deleteButton() {
				uni.navigateBack();
			}
		},
		watch: {
			week_s: function() {
				if (this.week_e < this.week_s) {
					this.week_e = this.week_s + '' - '0';
				}
				this.week_s = this.week_s + '' - '0';
			},
			week_e: function() {
				if (this.week_e < this.week_s) {
					this.week_s = this.week_e + '' - '0';
				}
				this.week_e = this.week_e + '' - '0';
			},
			weekType: function() {
				if (this.weekType + '' - '0' == 1) {
					if ((this.week_s + '' - '0') % 2 == 1) {
						this.week_s = this.week_s + '' - '0' - 1;
					}
					if ((this.week_e + '' - '0') % 2 == 1) {
						this.week_e = this.week_e + '' - '0' + 1;
						if (this.week_e >= 20) {
							this.week_e = 18;
						}
					}
				} else if (this.weekType + '' - '0' == 2) {
					if ((this.week_s + '' - '0') % 2 == 0) {
						this.week_s = this.week_s + '' - '0' - 1;
						if (this.week_s + '' - '0' < 0) {
							this.week_s = 1;
						}
					}
					if ((this.week_e + '' - '0') % 2 == 0) {
						this.week_e = this.week_e + '' - '0' + 1;
					}
				}
			}
		}
	}
</script>

<style>
	@import url("../addTest/addTest.css");
	@import url("./addCourse.css");
</style>
