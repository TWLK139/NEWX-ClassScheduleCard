<template>
	<view>
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view class="box_grade" style="margin-top: 0upx;" @click="ask()">
			<view class="flex_box_grade">
				<view id="all_title_grade">成绩总览</view>
				<image id="ask_image" mode="widthFix" src="../../static/grade/ask.png"></image>
				<view class="inline_word_box" style="width: auto;">
					<view class="title_word_grade">学分总计：</view>
					<view class="grade_word_grade" style="color: #F37B1D;">{{ all.all_credit }}</view>
				</view>
			</view>
			<view class="flex_box_grade flex_border">
				<view class="inline_word_box" style="width: auto;">
					<view class="title_word_grade">及格科目：</view>
					<view class="grade_word_grade">
						<text :class="[all.all == all.pass ? 'choose_green' : 'choose_red']">{{ all.pass }}</text>
						/
						<text style="color: #0D517B;">{{ all.all }}</text>
					</view>
				</view>
				<view class="inline_word_box" style="width: auto;">
					<view class="title_word_grade">平均绩点：</view>
					<view class="grade_word_grade" style="color: #F37B1D;">{{ all.all_grade }}</view>
				</view>
			</view>
			<view class="flex_box_grade">
				<view class="inline_word_box">
					<view class="title_word_grade">总分学分：</view>
				</view>
			</view>
			<view class="flex_box_grade flex_border">
				<view class="inline_word_box">
					<view class="title_word_grade">必修：</view>
					<view class="grade_word_grade" style="color: #6ab699;">{{ all.required_credit }}</view>
				</view>
				<view class="inline_word_box">
					<view class="title_word_grade">辅修：</view>
					<view class="grade_word_grade" style="color: #6eb561;">{{ all.minor_credit }}</view>
				</view>
				<view class="inline_word_box">
					<view class="title_word_grade">选修：</view>
					<view class="grade_word_grade" style="color: #9ad966;">{{ all.elective_credit }}</view>
				</view>
			</view>
			<view class="flex_box_grade">
				<view class="inline_word_box">
					<view class="title_word_grade">总分绩点：</view>
				</view>
			</view>
			<view class="flex_box_grade flex_border">
				<view class="inline_word_box">
					<view class="title_word_grade">必修：</view>
					<view class="grade_word_grade" style="color: #6ab699;">{{ all.required_grade }}</view>
				</view>
				<view class="inline_word_box">
					<view class="title_word_grade">辅修：</view>
					<view class="grade_word_grade" style="color: #6eb561;">{{ all.minor_grade }}</view>
				</view>
				<view class="inline_word_box">
					<view class="title_word_grade">选修：</view>
					<view class="grade_word_grade" style="color: #9ad966;">{{ all.elective_grade }}</view>
				</view>
			</view>
			<view class="flex_box_grade">
				<view class="inline_word_box">
					<view class="title_word_grade">总分加权均分：</view>
				</view>
			</view>
			<view class="flex_box_grade flex_border">
				<view class="inline_word_box">
					<view class="title_word_grade">必修：</view>
					<view class="grade_word_grade" style="color: #6ab699;">{{ all.required_average }}</view>
				</view>
				<view class="inline_word_box">
					<view class="title_word_grade">辅修：</view>
					<view class="grade_word_grade" style="color: #6eb561;">{{ all.minor_average }}</view>
				</view>
				<view class="inline_word_box">
					<view class="title_word_grade">选修：</view>
					<view class="grade_word_grade" style="color: #9ad966;">{{ all.elective_average }}</view>
				</view>
			</view>
		</view>

		<view class="box_grade" v-for="(theTrem, index) in trem" :key="grade_res[index].code" @click="setTremShow(index)">
			<view class="flex_box_grade" style="border-bottom: #979797 4upx solid;padding-bottom: 4upx;">
				<view class="trem_name">{{ grade_res[index].name }}</view>
				<view class="trem_season" :class="[grade_res[index].season == '春' ? 'choose_grass' : 'choose_harvest']">({{ grade_res[index].season }})</view>
			</view>
			<view class="flex_box_grade flex_border">
				<view class="inline_word_box" style="width: auto;">
					<view class="title_word_grade">学期学分：</view>
					<view class="grade_word_grade" style="color: #F37B1D;">{{ theTrem.all_credit }}</view>
				</view>
				<view class="inline_word_box" style="width: auto;">
					<view class="title_word_grade">学期绩点：</view>
					<view class="grade_word_grade" style="color: #F37B1D;">{{ theTrem.all_grade }}</view>
				</view>
			</view>
			<view class="flex_box_grade">
				<view class="inline_word_box">
					<view class="title_word_grade">学期学分：</view>
				</view>
			</view>
			<view class="flex_box_grade flex_border">
				<view class="inline_word_box">
					<view class="title_word_grade">必修：</view>
					<view class="grade_word_grade" style="color: #6ab699;">{{ theTrem.required_credit }}</view>
				</view>
				<view class="inline_word_box">
					<view class="title_word_grade">辅修：</view>
					<view class="grade_word_grade" style="color: #6eb561;">{{ theTrem.minor_credit }}</view>
				</view>
				<view class="inline_word_box">
					<view class="title_word_grade">选修：</view>
					<view class="grade_word_grade" style="color: #9ad966;">{{ theTrem.elective_credit }}</view>
				</view>
			</view>
			<view class="flex_box_grade">
				<view class="inline_word_box">
					<view class="title_word_grade">学期绩点：</view>
				</view>
			</view>
			<view class="flex_box_grade flex_border">
				<view class="inline_word_box">
					<view class="title_word_grade">必修：</view>
					<view class="grade_word_grade" style="color: #6ab699;">{{ theTrem.required_grade }}</view>
				</view>
				<view class="inline_word_box">
					<view class="title_word_grade">辅修：</view>
					<view class="grade_word_grade" style="color: #6eb561;">{{ theTrem.minor_grade }}</view>
				</view>
				<view class="inline_word_box">
					<view class="title_word_grade">选修：</view>
					<view class="grade_word_grade" style="color: #9ad966;">{{ theTrem.elective_grade }}</view>
				</view>
			</view>
			<view class="flex_box_grade">
				<view class="inline_word_box">
					<view class="title_word_grade">学期加权均分：</view>
				</view>
			</view>
			<view class="flex_box_grade flex_border">
				<view class="inline_word_box">
					<view class="title_word_grade">必修：</view>
					<view class="grade_word_grade" style="color: #6ab699;">{{ theTrem.required_average }}</view>
				</view>
				<view class="inline_word_box">
					<view class="title_word_grade">辅修：</view>
					<view class="grade_word_grade" style="color: #6eb561;">{{ theTrem.minor_average }}</view>
				</view>
				<view class="inline_word_box">
					<view class="title_word_grade">选修：</view>
					<view class="grade_word_grade" style="color: #9ad966;">{{ theTrem.elective_average }}</view>
				</view>
			</view>

			<view class="flex_box_grade">
				<view class="inline_word_box" style="width: auto;">
					<view class="title_word_grade">及格科目：</view>
					<view class="grade_word_grade">
						<text :class="[theTrem.all == theTrem.pass ? 'choose_green' : 'choose_red']">{{ theTrem.pass }}</text>
						/
						<text style="color: #0D517B;">{{ theTrem.all }}</text>
					</view>
				</view>
				<view class="inline_word_box">
					<view class="detail_word">成绩详情</view>
					<image class="image_grade" :class="[returnTremShow(index) ? 'choose_minus90' : 'choose_90']" src="../../static/next.png"></image>
				</view>
			</view>

			<view v-show="returnTremShow(index)" class="detail_box_lesson" v-for="(lesson, inLe) in grade_res[index].lessons"
			 :key="inLe" @click.stop="setDetailShow(index, inLe)">
				<image class="box_grade_bgi" mode="widthFix" v-if="getIisRequire(lesson.course_code) == 0" src="../../static/grade/require.png"></image>
				<image class="box_grade_bgi" mode="widthFix" v-else-if="getIisRequire(lesson.course_code) == 1" src="../../static/grade/minor.png"></image>
				<image class="box_grade_bgi" mode="widthFix" v-else-if="getIisRequire(lesson.course_code) == 2" src="../../static/grade/elective.png"></image>
				<image class="box_grade_bgi" mode="widthFix" v-else src="../../static/grade/unknow.png"></image>
				<view class="flex_box_detail">
					<view class="ellipsis_detail_box">{{ lesson.course_name }}</view>
					<view class="flex_box_detail_grade">
						<view class="flex_box_detail_grade">
							<view class="detail_grade_word_title">学分：</view>
							<view class="detail_grade_word_con">{{ lesson.course_credit }}</view>
						</view>
						<view class="flex_box_detail_grade">
							<view class="detail_grade_word_title">绩点：</view>
							<view class="detail_grade_word_con">{{ lesson.course_gp }}</view>
						</view>
					</view>
				</view>
				<view class="flex_box_detail_grade box_score">
					<view class="score_word" :class="[lesson.passed ? 'choose_pass' : 'choose_red', (lesson.score_text == '未评教' || lesson.score_text == '及格' || lesson.score_text == '不及格' || lesson.score_text == '未考') ? 'choose_txtSmall' : '']">
						{{ lesson.score_text }}
					</view>
					<image class="image_grade" v-show="lesson.score_text != '未评教'" :class="[returnDetailShow(index, inLe) ? 'choose_minus90' : 'choose_90']"
					 src="../../static/next.png"></image>
				</view>

				<view class="box_exam" v-show="returnDetailShow(index, inLe)">
					<view class="exam" v-for="(score, insc) in lesson.exam_grades" :key="insc">
						<view class="exam_title">{{ score.type }}：</view>
						<view class="exam_con" :class="[score.passed ? 'choose_pass' : 'choose_red']">{{ score.score }}</view>
					</view>
				</view>
			</view>
		</view>
		<view id="saveButton" @click="setSet()">设置</view>
		<view style="width: 100%;height: 200upx;"></view>
	</view>
</template>

<script>
	import Vue from 'vue';
	export default {
		data() {
			return {
				grade_res: [],
				trem: [],
				all: {
					required_credit: 0,
					required_grade: 0,
					elective_credit: 0,
					elective_grade: 0,
					all_credit: 0,
					all_grade: 0,
					pass: 0,
					all: 0
				},
				isRequire: {},
				trem_show: [],
				trem_flag: true,
				detial_show: [],
				detail_flag: true,
				student_id: ''
			};
		},
		onBackPress(event) {
			uni.switchTab({
				url: '../my/my'
			});
			return true;
		},
		onLoad() {
			this.student_id = uni.getStorageSync('student_id');
			this.getMessage();
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
					title: '加载中……'
				});
				uni.getStorage({
					key: 'grade_res' + this.student_id,
					success: res => {
						this.grade_res = res.data;
					},
					complete: res => {
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
								} else if (res.data.code == this.code.unLogin) {
									this.error.login();
								} else {
									this.error.school();
								}
							},
							fail: res => {
								uni.hideLoading();
								this.error.internet();
							},
							complete: res => {
								this.getSet();
							}
						});
					}
				});
			},
			computeData() {
				this.all = {
					required_credit: 0,
					required_grade: 0,
					required_average: 0,
					minor_credit: 0,
					minor_grade: 0,
					minor_average: 0,
					elective_credit: 0,
					elective_grade: 0,
					elective_average: 0,
					all_credit: 0,
					all_grade: 0,
					pass: 0,
					all: 0
				};
				this.trem_show = [];
				var trem = [];
				for (var i = 0; i < this.grade_res.length; i++) {
					var temArr = [];
					this.trem_show.push(true);
					this.detial_show.push(temArr);
					var grade_data = {
						required_credit: 0,
						required_grade: 0,
						required_average: 0,
						elective_credit: 0,
						elective_grade: 0,
						elective_average: 0,
						minor_credit: 0,
						minor_grade: 0,
						minor_average: 0,
						all_credit: 0,
						all_grade: 0,
						pass: 0,
						all: 0,
					};
					for (var j = 0; j < this.grade_res[i].lessons.length; j++) {
						this.detial_show[i].push(false);
						var tem = this.grade_res[i].lessons[j];
						//tem.course_code.substr(tem.course_code.length-1,1) == "X"
						if (tem.passed) {
							if (this.isRequire[tem.course_code] == 0) {
								grade_data.required_credit += tem.course_credit;
								grade_data.required_grade += tem.course_credit * tem.course_gp;
								grade_data.required_average += tem.course_credit * tem.score;
							} else if (this.isRequire[tem.course_code] == 1) {
								grade_data.minor_credit += tem.course_credit;
								grade_data.minor_grade += tem.course_credit * tem.course_gp;
								grade_data.minor_average += tem.course_credit * tem.score;
							} else if (this.isRequire[tem.course_code] == 2) {
								grade_data.elective_credit += tem.course_credit;
								grade_data.elective_grade += tem.course_credit * tem.course_gp;
								grade_data.elective_average += tem.course_credit * tem.score;
							} else if (tem.course_code.substr(tem.course_code.length - 1, 1) == 'B') {
								grade_data.required_credit += tem.course_credit;
								grade_data.required_grade += tem.course_credit * tem.course_gp;
								grade_data.required_average += tem.course_credit * tem.score;
							} else {
								grade_data.elective_credit += tem.course_credit;
								grade_data.elective_grade += tem.course_credit * tem.course_gp;
								grade_data.elective_average += tem.course_credit * tem.score;
							}
						}
						grade_data.all++;
						if (tem.passed) {
							grade_data.pass++;
						}
					}
					this.all.required_credit += grade_data.required_credit;
					this.all.required_grade += grade_data.required_grade;
					this.all.required_average += grade_data.required_average;
					this.all.elective_credit += grade_data.elective_credit;
					this.all.elective_grade += grade_data.elective_grade;
					this.all.elective_average += grade_data.elective_average;
					this.all.minor_credit += grade_data.minor_credit;
					this.all.minor_grade += grade_data.minor_grade;
					this.all.minor_average += grade_data.minor_average;
					this.all.all += grade_data.all;
					this.all.pass += grade_data.pass;
					grade_data.all_credit = grade_data.required_credit + grade_data.elective_credit + grade_data.minor_credit;
					grade_data.all_grade = grade_data.required_grade + grade_data.elective_grade + grade_data.minor_grade;
					if (grade_data.elective_credit == 0) {
						grade_data.elective_grade = 0;
						grade_data.elective_average = 0;
					} else {
						grade_data.elective_grade = (grade_data.elective_grade / grade_data.elective_credit).toFixed(2);
						grade_data.elective_average = (grade_data.elective_average / grade_data.elective_credit).toFixed(2);
					}
					if (grade_data.required_credit == 0) {
						grade_data.required_grade = 0;
						grade_data.required_average = 0;
					} else {
						grade_data.required_grade = (grade_data.required_grade / grade_data.required_credit).toFixed(2);
						grade_data.required_average = (grade_data.required_average / grade_data.required_credit).toFixed(2);
					}
					if (grade_data.minor_credit == 0) {
						grade_data.minor_grade = 0;
						grade_data.minor_average = 0;
					} else {
						grade_data.minor_grade = (grade_data.minor_grade / grade_data.minor_credit).toFixed(2);
						grade_data.minor_average = (grade_data.minor_average / grade_data.minor_credit).toFixed(2);
					}
					if (grade_data.all_credit == 0) {
						grade_data.all_grade = 0;
					} else {
						grade_data.all_grade = (grade_data.all_grade / grade_data.all_credit).toFixed(2);
					}
					trem.push(grade_data);
				}
				this.trem = trem;
				this.all.all_credit = this.all.required_credit + this.all.elective_credit + this.all.minor_credit;
				this.all.all_grade = this.all.required_grade + this.all.elective_grade + this.all.minor_grade;
				if (this.all.required_credit == 0) {
					this.all.required_grade = 0;
					this.all.required_average = 0;
				} else {
					this.all.required_grade = (this.all.required_grade / this.all.required_credit).toFixed(2);
					this.all.required_average = (this.all.required_average / this.all.required_credit).toFixed(2);
				}
				if (this.all.minor_credit == 0) {
					this.all.minor_grade = 0;
					this.all.minor_average = 0;
				} else {
					this.all.minor_grade = (this.all.minor_grade / this.all.minor_credit).toFixed(2);
					this.all.minor_average = (this.all.minor_average / this.all.minor_credit).toFixed(2);
				}
				if (this.all.elective_credit == 0) {
					this.all.elective_grade = 0;
					this.all.elective_average = 0;
				} else {
					this.all.elective_grade = (this.all.elective_grade / this.all.elective_credit).toFixed(2);
					this.all.elective_average = (this.all.elective_average / this.all.elective_credit).toFixed(2);
				}
				if (this.all.all_credit == 0) {
					this.all.all_grade = 0;
				} else {
					this.all.all_grade = (this.all.all_grade / this.all.all_credit).toFixed(2);
				}
			
				this.trem_flag = !this.trem_flag;
				this.detail_flag = !this.detail_flag;
				uni.showToast({
					title: '计算中……',
					icon: 'loading',
					duration: 2000
				});
			},
			getSet() {
				uni.getStorage({
					key: 'grade_isRequire' + this.student_id,
					success: res => {
						this.isRequire = res.data;
						if (!this.checkSet()) {
							uni.showModal({
								title: '数据不足',
								content: '当前存在新课程未设置属于选修或必修',
								showCancel: true,
								confirmText: '前往设置',
								success: res => {
									if (res.confirm) {
										uni.navigateTo({
											url: '../setGrade/setGrade'
										});
									}
								},
								complete: res => {
									this.computeData();
								}
							});
						} else {
							this.computeData();
						}
					},
					fail: res => {
						uni.showModal({
							title: '数据不足',
							content: '由于部分各学院规定不同，需先手动设置课程属于必修或选修',
							showCancel: true,
							confirmText: '前往设置',
							cancelText: '以后再说',
							success: res => {
								if (res.cancel) {
									this.computeData();
									uni.showToast({
										title: '未设置课程默认为必修',
										icon: 'none'
									});
								} else {
									uni.navigateTo({
										url: '../setGrade/setGrade'
									});
								}
							}
						});
					}
				});
			},
			checkSet() {
				for (var i = 0; i < this.grade_res.length; i++) {
					for (var j = 0; j < this.grade_res[i].lessons.length; j++) {
						if (!this.isRequire.hasOwnProperty(this.grade_res[i].lessons[j].course_code)) {
							return false;
						}
					}
				}
				return true;
			},
			setSet() {
				uni.navigateTo({
					url: '../setGrade/setGrade'
				});
			},
			setTremShow(i) {
				this.trem_show[i] = !this.trem_show[i];
				this.trem_flag = !this.trem_flag;
			},
			setDetailShow(i, j) {
				if (this.grade_res[i].lessons[j].course_gp == '') {
					uni.showModal({
						title: '未评教',
						content: '需要前往教务评教后才能查看详细成绩',
						showCancel: true,
						confirmText: '前往教务',
						cancelText: '以后再说',
						success: res => {
							if (res.confirm) {
								uni.setClipboardData({
									data: 'http://jxglstu.hfut.edu.cn/eams5-student/login&copy=1',
									success: () => {
										uni.showModal({
											title: '温馨提示',
											content: '教务网站的网址已经复制到剪贴板，快去浏览器粘帖吧！',
											showCancel: false,
											confirmText: '我知道了'
										});
									},
									fail: (res) => {
										uni.showModal({
											title: '温馨提示',
											content: '请使用浏览器打开网址：http://jxglstu.hfut.edu.cn/eams5-student/login&copy=1',
											showCancel: false,
											confirmText: '我知道了'
										})
									}
								});
							}
						}
					});
				} else {
					this.detial_show[i][j] = !this.detial_show[i][j];
					this.detail_flag = !this.detail_flag;
				}
			},
			ask() {
				uni.showModal({
					title: '提示',
					content: '如果您的课程属性显示为“未知”，则说明数据不完善，需要点击屏幕下方“设置”按钮完善信息；如果您认为成程归类错误（选修或必修显示错误），您也可以随时点击设置按钮前往修改；“未知”类型在计算学分、绩点时会被归为选修。',
					showCancel: false,
					confirmText: '了解'
				});
			}
		},
		computed: {
			returnTremShow() {
				return function(i) {
					if (this.trem_flag) return this.trem_show[i];
					else return this.trem_show[i];
				};
			},
			returnDetailShow() {
				return function(i, j) {
					if (this.detail_flag) return this.detial_show[i][j];
					else return this.detial_show[i][j];
				};
			},
			getIisRequire() {
				return function(index) {
					if (this.isRequire[index] == 0 || this.isRequire[index] == 1 || this.isRequire[index] == 2) {
						return this.isRequire[index];
					} else {
						if (index.substr(index.length - 1, 1) == 'B') {
							return 0;
						} else if (index.substr(index.length - 1, 1) == 'M') {
							return 2;
						} else {
							return -1;
						}
					}
				};
			}
		}
	};
</script>

<style>
	@import url('./grade.css');
</style>
