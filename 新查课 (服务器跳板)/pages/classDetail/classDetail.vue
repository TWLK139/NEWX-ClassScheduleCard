<template>
	<view>
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view id="box">
			<view class="editBox" style="font-size: 45upx;position: relative;">
				<view style="width: 85%;">{{ lesson.courseName }}</view>
				<view @click="gotoManger()" id="gotoSavePage">{{(type==1)?'修改':'管理'}}</view>
			</view>
			<view class="editBox">
				<view class="editName">课程代码：</view>
				<input class="editEdit_lesson" :value="lesson.courseNumber" :disabled="true"></input>
			</view>
			<view class="editBox">
				<view class="editName">班级：</view>
				<view class="editEdit_lesson">{{ lesson.class }}</view>
			</view>
			<view class="editBox">
				<view class="editName">班级代码：</view>
				<view class="editEdit_lesson">{{ lesson.classNumber }}</view>
			</view>
			<view class="editBox">
				<view class="editName samll_editName">学分：</view>
				<view class="editEdit_lesson samll_editEdit">{{ lesson.grade }}</view>
				<view class="editName samll_editName" style="border-left: #CCCCCC 2upx solid;padding-left: 25upx;">考核：</view>
				<view class="editEdit_lesson samll_editEdit">{{ lesson.method }}</view>
			</view>
			<view class="editBox">
				<view class="editName">教师：</view>
				<view class="editEdit_lesson">{{ lesson.teacher }}</view>
			</view>
			<view class="editBox">
				<view class="editName">教师等级：</view>
				<view class="editEdit_lesson">{{ lesson.teacherLevel }}</view>
			</view>
			<view class="editBox">
				<view class="editName">时间地点：</view>
				<view class="editBox_lesson" v-for="(tp, i) in lesson.timePlace" :key="i">
					<view class="editEdit_lesson" style="width: 100%;border: none;">时间：{{ showTime(i) }}</view>
					<view class="editEdit_lesson" style="width: 100%;border: none;">地点：{{ showPlace(i) }}</view>
				</view>
			</view>
			<view class="editBox">
				<view class="editName">课程类型：</view>
				<view class="editEdit_lesson">{{ lesson.courseType }}</view>
			</view>
			<view class="editBox">
				<view class="editName">开课学期：</view>
				<view class="editEdit_lesson">{{ lesson.courseTerm }}</view>
			</view>
			<view class="editBox">
				<view class="editName">备注：</view>
				<textarea class="editEdit_arer" maxlength="200" v-model="lesson.remarks" placeholder="课程备注(收藏后才能备注哦)" ></textarea>
			</view>
			<view class="editBox" style="flex-wrap: nowrap;border-bottom: none;">
				<view class="saveButton" style="background-color: #3681BA;" @click="saveButton()">{{(saveFlag||type==1)?'保存':'保存并收藏'}}</view>
				<view class="saveButton" v-if="saveFlag || type == 1" style="width: 10%;"></view>
				<view class="saveButton" v-if="saveFlag || type == 1" style="background-color: #DD524D;" @click="deleteButton()">删除</view>
			</view>
		</view>
		<view style="width: 100%;height: 100upx;"></view>
	</view>
</template>

<script>
	import Vue from 'vue';
	export default{
		data() {
			return {
				student_id:'0000000000',
				lesson:{},
				saveFlag:false,
				lessonSave:{},
				type:0,
				index:0,
				trem:'',
				class_local:{}
			}
		},
		onLoad(option) {
			// type == 1表示跳转来自课表页面
			if (option.type!=null) {
				this.type = option.type;
				this.index = option.index;
				this.student_id = option.id;
				this.trem = option.trem;
				uni.getStorage({
					key: 'class_local' + this.trem + this.student_id,
					success: res => {
						this.class_local = res.data;
						if (this.class_local[option.index] != null) {
							this.lesson = this.class_local[this.index];
						} else {
							uni.showToast({
								title:'课程不存在'
							});
							uni.navigateBack();
						}
					},
					fail: res => {
						uni.showToast({
							title:'课程不存在'
						});
						uni.navigateBack();
					}
				});
			} else {
				uni.getStorage({
					key: 'lessonToSee',
					success: (res) => {
						this.lesson = res.data;
					},
					fail: (res) => {
						uni.showModal({
							title:'错误！',
							content:'系统发生未知错误，请联系NEWX工作室，感谢您的支持！',
							showCancel:false,
							confirmText:'确认',
							success: (res) => {
								uni.navigateBack();
							}
						});
					},
					complete: (res) => {
						uni.getStorage({
							key:'student_id',
							success:(res)=>{
								this.student_id = res.data;
							},
							complete: (res) => {
								uni.getStorage({
									key:'lessonSave' + this.student_id,
									success: (res) => {
										this.lessonSave = res.data;
									},
									fail: (res) => {
										this.lessonSave = {};
									},
									complete: (res) => {
										if(this.lessonSave[this.lesson.classNumber] != null) {
											this.saveFlag = true;
											this.lesson = res.data[this.lesson.classNumber];
										} else {
											this.saveFlag = false;
											this.lesson.remarks = '';
										}
									}
								})
							}
						});
					}
				});
			}
			
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods:{
			saveButton() {
				if (this.type == 1) {
					this.class_local[this.index] = this.lesson;
					uni.setStorage({
						key:'class_local' + this.trem + this.student_id,
						data:this.class_local,
						success: (res) => {
							uni.showModal({
								title:'成功',
								content:'保存成功！',
								showCancel:false
							})
						},
						fail: (res) => {
							uni.showModal({
								title:'失败',
								content:'保存失败',
								showCancel:false
							})
						}
					});
				} else {
					uni.showLoading({
						title:'保存中……'
					});
					this.lessonSave[this.lesson.classNumber] = this.lesson;
					uni.setStorage({
						key:'lessonSave' + this.student_id,
						data:this.lessonSave,
						success: (res) => {
							uni.hideLoading();
							uni.showToast({
								title:'保存成功！',
								duration:2000,
								mask:true
							});
							setTimeout(()=>{
								uni.navigateBack();
							},1900);
						},
						fail: (res) => {
							uni.hideLoading();
							uni.showToast({
								title:'保存失败',
								icon:'none',
								duration:2000
							});
						}
					});
				}
			},
			deleteButton() {
				if (this.type == 1) {
					uni.showModal({
						title:'请确认',
						content:'确定要删除该自定义课程？删除后将失去关于该课程的所有信息。',
						showCancel:true,
						cancelText:'点错了',
						confirmText:'确定',
						success: (res) => {
							if (res.confirm) {
								uni.showLoading({
									title:'正在删除……',
									mask:true
								});
								this.class_local.splice(this.index, 1);
								uni.setStorage({
									key:'class_local' + this.trem + this.student_id,
									data:this.class_local,
									success: (res) => {
										uni.hideLoading();
										uni.showToast({
											title:'删除成功！',
											duration:1000,
											mask:true
										});
										setTimeout(()=>{
											let pages = getCurrentPages();
											let prevPage = pages[pages.length - 2];
											prevPage.$vm.shouldRefresh = true;
											uni.navigateBack();
										},900);
									},
									fail: (res) => {
										uni.hideLoading();
										uni.showToast({
											title:'删除失败',
											icon:'none',
											duration:1000
										});
									}
								});
							}
						}
					});
				} else {
					uni.showModal({
						title:'请确认',
						content:'确定要删除该收藏课程？删除后将失去关于该课程的备注信息。',
						showCancel:true,
						cancelText:'点错了',
						confirmText:'确定',
						success: (res) => {
							if (res.confirm) {
								uni.showLoading({
									title:'正在删除……',
									mask:true
								});
								delete this.lessonSave[this.lesson.classNumber];
								uni.setStorage({
									key:'lessonSave' + this.student_id,
									data:this.lessonSave,
									success: (res) => {
										uni.hideLoading();
										uni.showToast({
											title:'删除成功！',
											duration:1000,
											mask:true
										});
										this.saveFlag = false;
									},
									fail: (res) => {
										uni.hideLoading();
										uni.showToast({
											title:'删除失败',
											duration:1000
										});
									}
								});
							}
						}
					});
				}
			},
			gotoManger() {
				if(this.type != 1) {
					uni.navigateTo({
						url:'../classSave/classSave'
					});
				} else {
					uni.navigateTo({
						url: '../addCourse/addCourse?num=' + this.trem + '&type=1&id='+this.student_id+'&index='+this.index
					});
				}
			}
		},
		computed:{
			showTime() {
				return function(index) {
					let res = '';
					
					if (parseInt((this.lesson.timePlace[index].week) / 100) == ((this.lesson.timePlace[index].week) % 100)) {
						res += "第" + parseInt((this.lesson.timePlace[index].week) / 100) + "周";
					} else {
						res += "第" + parseInt((this.lesson.timePlace[index].week) / 100) + "-" + ((this.lesson.timePlace[index].week) % 100) + "周";
					}
					
					if (this.lesson.timePlace[index].type == 0) {
						res += "单双周，";
					} else if (this.lesson.timePlace[index].type == 1) {
						res += "单周，";
					} else if (this.lesson.timePlace[index].type == 2) {
						res += "双周，";
					}
					
					res += ("星期" + parseInt((this.lesson.timePlace[index].lesson) / 10000)) + "，第" +
						parseInt(((this.lesson.timePlace[index].lesson) % 10000) / 100) + "-" + ((this.lesson.timePlace[index].lesson) % 100) + "节";
					
					return res;
				}
			},
			showPlace() {
				return function(index) {
					let res = "";
								
					if (this.lesson.timePlace[index].place < 1000) {
						res += "其他";
						if (this.lesson.timePlace[index].other != null) {
							res += this.lesson.timePlace[index].other;
						}
					} else if (this.lesson.timePlace[index].place < 2000) {
						res += "敬亭" + ((this.lesson.timePlace[index].place) % 1000);
					} else if (this.lesson.timePlace[index].place < 3000) {
						res += "新安" + ((this.lesson.timePlace[index].place) % 2000);
					} else if (this.lesson.timePlace[index].place < 4000) {
						res += "计算机中心" + ((this.lesson.timePlace[index].place) % 3000);
					} else if (this.lesson.timePlace[index].place < 5000) {
						res += "综合实验楼一" + ((this.lesson.timePlace[index].place) % 4000);
					} else if (this.lesson.timePlace[index].place < 6000) {
						res += "综合实验楼二" + ((this.lesson.timePlace[index].place) % 5000);
					} else if (this.lesson.timePlace[index].place < 7000) {
						res += "工程训练中心" + ((this.lesson.timePlace[index].place) % 6000);
					} else if (this.lesson.timePlace[index].place < 8000) {
						res += "化工楼" + ((this.lesson.timePlace[index].place) % 7000);
					} else if (this.lesson.timePlace[index].place < 9000) {
						res += "风雨操场";
					} else if (this.lesson.timePlace[index].place < 10000) {
						res += "体育馆" + ((this.lesson.timePlace[index].place) % 9000);
					}
			
					return res;
				}
			}
		}
	}
</script>

<style>
@import url("./classDetail.css");
</style>
