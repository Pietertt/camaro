<template>
    <div class="uk-section uk-section-muted">
        <h1>{{ $route.params.id }}</h1>

        <video controls>
            <source v-if="loaded" v-bind:src=videoSource>
        </video>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator';
    import axios from 'axios';
    import VueRouter, { Route } from 'vue-router';
    
    import MenuComponent from '@/components/dashboard/MenuComponent.vue';
    import ActionsComponent from '@/components/dashboard/ActionsComponent.vue';
    import MonthlyComponent from '@/components/dashboard/MonthlyComponent.vue';
    import ActivitiesComponent from '@/components/dashboard/ActivitiesComponent.vue';
    import StatisticsComponent from '@/components/dashboard/StatisticsComponent.vue';
    import LoginService from '../services/LoginService';

    @Component({
        components: {
            MenuComponent
        }
    })
    export default class Activities extends Vue {
        private recentData = [];
        private videoSource = '';
        private loaded = false;

        mounted(): void {
            this.loadActivities();
            setTimeout(function(){this.getName(this.$route.params.id)}.bind(this), 500);
        }


        loadActivities(): void {
            console.log('load activities function');
            axios.get('http://imac-van-pieter.local:5000/activities/all').then(response => {
                this.recentData = response.data;
            });
        }

        getName(currentId: string){
            for (const id of this.recentData){
                console.log(id[0])
                if (id[0] == currentId){
                    console.log('got m!');
                    //alert('you currently have ' + id[1] + '.mp4 selected')
                    this.videoSource = 'videos/' + String(id[1]) + '.mp4';
                    this.loaded = true;
                }
            }
        }
    }
    
</script>