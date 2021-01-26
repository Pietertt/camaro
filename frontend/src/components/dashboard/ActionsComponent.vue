
<template>
   <div class="uk-card uk-card-default">
        <div class="uk-card-body">
        <h3 class="uk-card-title">Sensordata</h3>
            <template v-if="data.length > 0">
                <span>
                    <span class="uk-margin-small-left uk-icon" uk-icon="rss"></span>
                    {{data[0]}}
                </span>
                <span>
                    <span class="uk-margin-small-left uk-icon" uk-icon="soundcloud"></span>
                    {{data[1]}}
                </span>
            </template>

            <template v-if="data.length == 0">
                <div class="uk-placeholder uk-text-center">Geen gegevens beschikbaar</div>
            </template>
        </div>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'
    import axios from 'axios'
    import { User } from '../../models/User';
    import LoginService from '../../services/LoginService';
    
    @Component
    export default class ActionsComponent extends Vue {

        private data: number[] = [];
        private loaded = false;
        private user: User = new User();

        mounted(): void {
            setTimeout(this.validate, 1000);
        }
        
       validate(): void {
            this.user = LoginService.getUserData();
            axios.get('http://imac-van-pieter.local:5000/sensor/value/recent?userid=' + this.user.id).then(response => {
                if (response.data.length > 0) {
                    this.data.push(response.data[0][0]);
                    this.data.push(response.data[0][1]);
                    this.loaded = true; 
                }
            });
        }
    }
    
</script>