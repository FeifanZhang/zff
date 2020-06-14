<template>
    <div class="ShowPhotos">
        <vue-waterfall-easy class="waterfall" ref="waterfall" :maxCols="this.maxCols" @scrollReachBottom="getphotos" :imgsArr="this.photos" :gap="this.gap" >
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
        methods:{
            getphotos(){
                if (this.$route.query.token === undefined) {
                    this.$router.replace({path: '/login'})
                }else {
                    this.token = this.$route.query.token;
                    photoRequest({
                        method: 'get',
                        params: {
                            token: this.token
                        }
                    }).then(res => {
                        if (this.photos.length > 0){
                            console.log("1");
                            this.$refs.waterfall.waterfallOver();
                            return
                        }
                        for (let a in res.data.photos){
                            console.log("222");
                            res.data.photos[a]['src'] = 'http://127.0.0.1:8000/media/' + res.data.photos[a]['src'];
                            this.photos.push(res.data.photos[a])
                        }
                    }).catch(res => {
                        console.log(res.response.status);
                        if(res.response.status === 403){
                            this.$router.replace({path: '/login'});
                        }
                    });
                }
            }
        },
        created() {
            this.getphotos()
        },
        // destroyed() {
        //     console.log("111");
        //     console.log(this.photos)
        // }
    }
</script>
<style>
    .img-info>h4{
        letter-spacing: 5px;
        background-color: transparent;
        margin-bottom: 0;
        margin-top: 0;
        color: #FFF1F0;
    }
	.ShowPhotos{
		margin-left: 0;
		margin-top: 1vh;
		width: 100%;
        height: 100%;
		background-color: rgba(0, 0, 0, 0);
		border-radius: 20px;
	}
</style>
