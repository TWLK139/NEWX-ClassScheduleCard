<template>
	<view>
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view id="box">
			<view id="examEditMask" v-if="mode == 1" @click="showStopEdit()"></view>
			<view class="editBox">
				<view class="editName">事件名称：</view>
				<input class="editEdit" maxlength="10" v-model="eventData.course_name" placeholder="新建备忘"></input>
			</view>
			<view class="editBox">
				<view class="editName samll_editName">标记：</view>
				<input class="editEdit samll_editEdit" maxlength="4" v-model="eventData.title_word" :placeholder="mode == 1?'考试':'我的'"></input>
				<view class="editName samll_editName" style="border-left: #CCCCCC 2upx solid;padding-left: 25upx;">类型：</view>
				<input class="editEdit samll_editEdit" maxlength="4" v-model="eventData.exam_type" placeholder="我的事件"></input>
			</view>
			<view class="editBox" style="justify-content: space-around;">
				<view class="editName" style="width: 100%;">标记颜色选择：</view>
				<view class="colorBlock" v-for="(color, index) in colors" :key="index" :style="{'backgroundColor':color}" @click="changeColor(index)">
					<view v-show="index == eventData.title_color" class="choose_font">&#10004</view>
				</view>
			</view>
			<view class="editBox">
				<view class="editName">日期：</view>
				<picker mode="date" :value="eventData.date" :start="getDataRange(0, 0, 0)" :end="getDataRange(1, 0, 0)" @change="bindDateChange">
					<view class="editEdit">{{eventData.date}}</view>
				</picker>
			</view>
			<view class="editBox">
				<view class="editName">起止时间：</view>
				<picker mode="time" :value="eventData.time_start" :start="getTimeRange(0, 0)" end="23:30" @change="bindStartTimeChange">
					<view class="editEdit samll_editEdit">{{eventData.time_start}}</view>
				</picker>
				<view class="lineTo"></view>
				<picker mode="time" :value="eventData.time_end" :start="eventData.time_start" end="24:00" @change="bindEndTimeChange">
					<view class="editEdit samll_editEdit">{{eventData.time_end}}</view>
				</picker>
			</view>
			<view class="editBox">
				<view class="editName">地点：</view>
				<input class="editEdit" maxlength="12" v-model="eventData.room_name" placeholder="地点未知"></input>
			</view>
			<view class="editBox" v-if="mode == 1">
				<view class="editName">课程代码：</view>
				<input class="editEdit" maxlength="10" v-model="eventData.lesson_code" placeholder="课程代码"></input>
			</view>
			<view class="editBox">
				<view class="editName">备注：</view>
				<textarea class="editEdit_arer" maxlength="200" v-model="remarks" placeholder="事件备注"></textarea>
			</view>
			<view class="editBox" style="flex-wrap: nowrap;border-bottom: none;">
				<view class="saveButton" style="background-color: #3681BA;" @click="saveButton()">保存</view>
				<view class="saveButton" v-if="mode == 2" style="width: 10%;"></view>
				<view class="saveButton" v-if="mode == 2" style="background-color: #DD524D;" @click="deleteButton()">删除</view>
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
				eventData: {
					title_word: '',
					title_color: 3,
					course_name: '',
					date: new Date().toISOString().slice(0, 10),
					exam_type: '',
					is_completed: false,
					lesson_code: '',
					room_name: '',
					time_end: new Date((new Date().getTime()) + 3600000).toTimeString().slice(0, 5),
					time_start: new Date().toTimeString().slice(0, 5),
				},
				mode: '',
				index: '',
				remarks: '',
				colors: ['#ff0000', '#F37B1D', '#39B54A', '#3681BA', '#6739B6', '#000000'],
				aimDatas: {},
				aimTrem: '',
				aimFinished: {},
				student_id: '',
				aimMore: {}
			};
		},
		onLoad(option) {
			this.aimTrem = option.code;
			this.mode = option.mode;
			this.index = option.index;
			if (option.mode != '1') {
				this.getFun("exam_local", "local_finished", "local_more")
			} else {
				this.getFun("exam_online", "exam_finished", "exam_more");
			}
		},
		onShow() {
			this.simpleCheck();
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			getFun(keyType, keyFinish, keyMore) {
				this.student_id = uni.getStorageSync('student_id');
				uni.getStorage({
					key: keyType + this.student_id,
					success: (res) => {
						this.aimDatas = res.data;
					},
					fail: (res) => {
						this.aimDatas = {}
					},
					complete: (res) => {
						if (this.mode != '0') {
							this.eventData = this.aimDatas[this.aimTrem][this.index];
						}
						if (this.mode == '1') {
							this.eventData.title_color = 0;
						}
					}
				});
				uni.getStorage({
					key: keyFinish + this.student_id,
					success: (res) => {
						this.aimFinished = res.data;
					},
					fail: (res) => {
						this.aimFinished = {}
					}
				});
				uni.getStorage({
					key: keyMore + this.student_id,
					success: (res) => {
						this.aimMore = res.data;
					},
					fail: (res) => {
						this.aimMore = {}
					},
					complete: (res) => {
						if (this.mode != '0') {
							this.remarks = this.aimMore[this.aimTrem][this.index];
						}
					}
				});
			},
			getDataRange(addY, addM, addD) {
				const date = new Date();
				let year = date.getFullYear() + addY;
				let month = date.getMonth() + 1 + addM;
				let day = date.getDate() + addD;

				month = month > 9 ? month : '0' + month;
				day = day > 9 ? day : '0' + day;
				return `${year}-${month}-${day}`;
			},
			bindDateChange(e) {
				this.eventData.date = e.target.value
			},
			getTimeRange(addH, addM) {
				if (this.eventData.date == new Date().toISOString().slice(0, 10)) {
					return new Date((new Date().getTime()) + addH * 3600000 + addM * 60000).toTimeString().slice(0, 5);
				} else {
					return '00:00'
				}
			},
			bindStartTimeChange(e) {
				this.eventData.time_start = e.target.value;
			},
			bindEndTimeChange(e) {
				this.eventData.time_end = e.target.value;
			},
			changeColor(index) {
				this.eventData.title_color = index;
			},
			saveButton() {
				uni.showLoading({
					title: '正在保存……'
				});
				this.checkData();
				if (this.aimDatas[this.aimTrem] == undefined) {
					this.aimDatas[this.aimTrem] = []
				}
				if (this.aimFinished[this.aimTrem] == undefined) {
					this.aimFinished[this.aimTrem] = [];
				}
				if (this.aimMore[this.aimTrem] == undefined) {
					this.aimMore[this.aimTrem] = [];
				}
				if (this.mode == '0') {
					this.aimDatas[this.aimTrem].unshift(this.eventData);
					this.aimFinished[this.aimTrem].unshift(false);
					this.aimMore[this.aimTrem].unshift(this.remarks);
				} else {
					this.aimDatas[this.aimTrem][this.index - '0'] = this.eventData;
					this.aimMore[this.aimTrem][this.index - '0'] = this.remarks;
				}
				if (this.mode != '1') {
					this.saveFun("exam_local", "local_finished", "local_more", "保存成功！");
				} else {
					this.saveFun("exam_online", "exam_finished", "exam_more", "保存成功！");
				}
			},
			checkData() {
				if (this.eventData.title_word == '') {
					this.eventData.title_word = '我的';
				}
				if (this.eventData.course_name == '') {
					this.eventData.course_name = '新建备忘';
				}
				if (this.eventData.exam_type == '') {
					this.eventData.exam_type = '我的事件';
				}
				if (this.eventData.room_name == '') {
					this.eventData.room_name = '地点无';
				}
			},
			saveFun(keyType, keyFinish, keyMore, message) {
				uni.setStorage({
					key: keyFinish + this.student_id,
					data: this.aimFinished
				});
				uni.setStorage({
					key: keyMore + this.student_id,
					data: this.aimMore
				});
				uni.setStorage({
					key: keyType + this.student_id,
					data: this.aimDatas,
					success: (res) => {
						uni.hideLoading();
						uni.showToast({
							title: message,
							duration: 2000,
							mask: true
						});
						setTimeout(function() {
							uni.navigateTo({
								url: '../test/test'
							})
						}, 2000);
					},
					fail: (res) => {
						uni.hideLoading();
						uni.showToast({
							title: '保存失败！',
							icon:'none'
						});
					}
				});
			},
			showStopEdit() {
				uni.showModal({
					title: '提示',
					content: '该考试信息来自于学校教务系统，内容不允许修改，但您可以尝试添加备注信息！',
					showCancel: false,
					confirmText: '了解'
				});
			},
			deleteButton() {
				uni.showModal({
					title: '请确认',
					content: '您确定要删除这条备忘录？',
					showCancel: true,
					cancelText: '点错了',
					confirmText: '确定',
					confirmColor: '#DD514C',
					cancelColor: '#0FB045',
					success: (res) => {
						if (res.confirm) {
							this.aimDatas[this.aimTrem].splice(this.index, 1);
							this.aimFinished[this.aimTrem].splice(this.index, 1);
							this.aimMore[this.aimTrem].splice(this.index, 1);

							this.saveFun("exam_local", "local_finished", "local_more", "删除成功！");
						}
					}
				});
			}
		}
	};
</script>

<style>
	@import url("./addTest.css");
</style>
