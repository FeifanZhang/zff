<template>
    <div class="ShowPhotos">
    <vue-waterfall-easy :maxCols="this.maxCols" :imgsArr="this.photos" :gap="this.gap" >
        <div class="img-info" slot-scope="props">
            <h4 class="some-info">{{props.value.info}}</h4>
        </div>
    </vue-waterfall-easy>
    </div>
</template>
<script>
    import vueWaterfallEasy from 'vue-waterfall-easy'
    import {photoRequest} from "../../request";
	export default {
        name: 'Photos',
        data() {
            return {
                token: '',
                photos: [],
            }
        },
        props: {
            gap: { // 图片间隔
                type: Number,
                default: 25
            },
            maxCols: { // 最大的列数
                type: Number,
                default: 4
            },
            timeOut: { // 预加载事件小于500毫秒就不显示加载动画，增加用户体验
                type: Number,
                default: 500
            }
        },
        components: {
            vueWaterfallEasy
        },
        created() {
            if (this.$route.query.token === undefined) {
                this.$router.replace({path: '/login'})
            } else {
                this.token = this.$route.query.token;
                photoRequest({
                    method: 'get',
                    params: {
                        token: this.token
                    }
                }).then(res => {
                    for (let a in res.data.photos){
                        res.data.photos[a]['src'] = 'http://127.0.0.1:8000/media/' + res.data.photos[a]['src'];
                        this.photos.push(res.data.photos[a])
                    }
                    console.log(this.photos);
                }).catch(res => {
                    console.log(res);
                })
            }
        },
    }
</script>
<style>
    .img-info>h4{
        letter-spacing: 5px;
        background-color: rgba(0, 0, 0, .3);
        margin-bottom: 0;
        margin-top: 0;
    }
	.ShowPhotos{
        position: absolute;
		margin-left: 0;
		margin-top: 1vh;
		width: 72vw;
        height: 70vh;
		background-color: rgba(0, 0, 0, 0);
		border-radius: 20px;
	}
</style>
