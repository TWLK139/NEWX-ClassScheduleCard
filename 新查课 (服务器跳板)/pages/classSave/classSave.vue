<template>
	<view>
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view id="res_box">
			<view class="lesson_box" v-for="(code, i) in lessonCodeArray" :key="i" @click="gotoDetail(lessonSave[code])">
				<!--  -->
				<view class="lesson_title">
					<view class="lesson_title_con ellipsis_div" style="text-align: left;">{{ lessonSave[code].courseName }}</view>
					<view class="lesson_title_con ellipsis_div" style="text-align: right;">教师:{{ lessonSave[code].teacher }}</view>
				</view>
				<view class="lesson_body">
					<view class="lesson_body_grade_box">
						<view class="lesson_body_grade_text" style="font-size: 30upx;color: #007aff;">学分</view>
						<view class="lesson_body_grade_text" style="font-size: 50upx;color: #007aff;">{{ lessonSave[code].grade }}</view>
					</view>
					<view class="lesson_body_describe">
						<view class="lesson_body_con ellipsis_div" style="margin-bottom: 20upx;">{{ lessonSave[code].class }}</view>
						<view class="lesson_body_con ellipsis_div">{{ lessonSave[code].courseType }}</view>
					</view>
					<view class="lesson_body_button">
						<view style="margin-bottom: 20upx;color: #ff0000;" @click.stop="toDelete(lessonSave[code])">删除</view>
						<view style="color: #848484;">详情</view>
					</view>
				</view>
				<view class="lesson_foot">{{ lessonSave[code].courseTerm }}</view>
			</view>
		</view>
		<view @click="gotoQuery()" id="gotoQuery" v-if="Object.keys(lessonSave).length == 0">
			<image id="queryImg" mode="widthFix" src="../../static/empty.png"></image>
			<view id="queryWord">目前还没有收藏课程哦，快点击这里去搜索课程吧！</view>
		</view>
	</view>
</template>

<script>
	import Vue from 'vue';
	export default {
		data() {
			return {
				student_id: '0000000000',
				lessonSave: {},
				lessonCodeArray: []
			}
		},
		onShow() {
			uni.getStorage({
				key: 'student_id',
				success: (res) => {
					this.student_id = res.data;
				},
				complete: (res) => {
					uni.getStorage({
						key: 'lessonSave' + this.student_id,
						success: (res) => {
							this.lessonSave = res.data;
							this.lessonCodeArray = Object.keys(this.lessonSave);
							this.$forceUpdate();
						},
						fail: (res) => {
							this.lessonSave = {};
						}
					})
				}
			});
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			gotoDetail(mes) {
				uni.showLoading({
					title: '查询中……'
				});
				uni.setStorage({
					key: 'lessonToSee',
					data: mes,
					success: (res) => {
						uni.hideLoading();
						uni.navigateTo({
							url: '../classDetail/classDetail'
						});
					},
					fail: (res) => {
						uni.hideLoading();
						uni.showModal({
							title: '程序异常',
							showCancel: false,
							confirmText: '确认'
						});
					}
				})
			},
			toDelete(mes) {
				uni.showModal({
					title: '请确认',
					content: '确定要删除该收藏课程？删除后将失去关于该课程的备注信息。',
					showCancel: true,
					cancelText: '点错了',
					confirmText: '确定',
					success: (res) => {
						if (res.confirm) {
							uni.showLoading({
								title: '正在删除……',
								mask: true
							});
							delete this.lessonSave[mes.classNumber];
							this.lessonCodeArray = Object.keys(this.lessonSave);
							uni.setStorage({
								key: 'lessonSave' + this.student_id,
								data: this.lessonSave,
								success: (res) => {
									uni.hideLoading();
									uni.showToast({
										title: '删除成功！',
										duration: 1000,
										mask: true
									});
									this.$forceUpdate();
								},
								fail: (res) => {
									uni.hideLoading();
									uni.showToast({
										title: '删除失败',
										icon: 'none',
										duration: 1000
									});
								}
							});
						}
					}
				});
			},
			gotoQuery() {
				uni.switchTab({
					url: '../query/query'
				})
			}
		}
	}
</script>

<style>
	@import url("../query/query.css");

	#gotoQuery {
		width: 95%;
		margin: 0 auto;
		padding: 200upx 0upx;
		display: flex;
		flex-direction: row;
		justify-content: center;
		flex-wrap: wrap;
	}

	#queryWord {
		width: 100%;
		font-size: 40upx;
		text-align: center;
		color: #8a8a8a;
	}

	#queryImg {
		width: 60%;
		margin-bottom: 20upx;
	}
</style>
