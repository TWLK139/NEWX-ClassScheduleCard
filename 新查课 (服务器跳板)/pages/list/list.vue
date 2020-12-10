<template>
	<view id="question">
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view class="questionList" :style="[{'height': queList.flag?'':'60px'}]" v-for="(queList,index) in questionList" :key="index"
		 @click="showAll(queList)">
			<view>
				<image src="../../static/list/que.png" class="QPic"></image>
				<view class="queTitle">
					<view :style="[{'width': '75%'}, {'height': queList.flag?'':'20px'}]" :class="[{'ellipsisView':!queList.flag}]">{{ queList.title }}</view>
					<view style="color: #a8a8a8;font-size: 80%;margin-right: 2%;">(点击{{ queList.flag?'收起':'查看' }})</view>
				</view>
			</view>
			<view>
				<image src="../../static/list/APic.png" class="QPic"></image>
				<view class="queCon" :style="[{'height': queList.flag?'':'15px'},{'overflow':'hidden'}]" v-html="queList.content"></view>
			</view>
		</view>
		<view id="noMore">
			没有更多了哦
		</view>
	</view>
</template>

<script>
	import Vue from 'vue';
	export default {
		data() {
			return {
				questionList: [],
			}
		},
		onLoad() {
			uni.request({
				url: Vue.config.baseUrl[3] + 'help',
				method: 'GET',
				header: {
					'content-type': 'application/x-www-form-urlencoded',
				},
				success: (res) => {
					if (res.data.code == this.code.success) {
						this.questionList = res.data.data;
						for (let i = 0; i < this.questionList.length; i++) {
							this.questionList[i].flag = false;
						}
					} else {
						this.error.server();
					}
				},
				fail: (res) => {
					this.error.internet();
				}
			})
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			showAll(ob) {
				ob.flag = !ob.flag
				this.$forceUpdate();
			}
		}
	}
</script>

<style>
	#question {
		width: 100%;
	}

	#questionTitle {
		width: 100%;
		height: 80upx;
		padding: 40upx 0 0 40upx;
		display: flex;
		flex-direction: row;
		background-color: white;
		position: fixed;
		top: 0;
		left: 0;
		border-bottom: #ececec 2px solid;
		color: #a8a8a8;
		z-index: 999;
	}

	#questionTitle>view {
		margin: 5upx 0 0 200upx;
	}

	.questionList {
		width: 90%;
		padding: 2% 2.5% 2% 2.5%;
		margin: 50upx auto;
		overflow: hidden;
		background-color: white;
		font-size: 30upx;
		border-radius: 10upx;
		box-shadow: 0 5upx 15upx #919191;
		display: flex;
		flex-direction: column;
		justify-content: space-around;
		position: relative;
		transition: all 0.5s ease;
	}

	.QAPic {
		width: 80upx;
		height: 80upx;
		position: absolute;
		top: -130%;
		right: 2%;
	}

	.questionList>view {
		position: relative;
		display: flex;
		flex-direction: row;
		align-items: center;
	}

	.QPic {
		width: 45upx;
		height: 45upx;
		margin-right: 1%;
	}

	.queTitle {
		width: 90%;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: flex-end;
	}

	.queCon {
		width: 90%;
		font-size: 90%;
		color: #878787;
	}

	.ellipsisView {
		overflow: hidden;
		white-space: nowrap;
		text-overflow: ellipsis;
	}

	#noMore {
		width: 100%;
		height: 100upx;
		display: flex;
		flex-direction: column;
		justify-content: center;
		text-align: center;
		color: #c1c1c1;
	}

	#bgimg {
		position: fixed;
		z-index: -1;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
	}
</style>
