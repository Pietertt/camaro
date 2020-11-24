<template>
    <div class="uk-card uk-card-default uk-card-body">
        <h3 class="uk-card-title">Percentage</h3>
        <Pie
      :data="[this.data[0], this.data[1]]"
      :labels="['Valid', 'Invalid']"
      :colors="['#1E87F0', '#222222']"
      :title="'Activiteiten'"
    />
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'
    import axios from 'axios'

    import Pie from '../charts/Pie.vue'

    @Component({
        components: {
            Pie
        }
    })

    export default class StatisticsComponent extends Vue {
        
        private data: number[] = [];

        mounted(): void {
            setTimeout(this.validate, 3000);
        }

        validate(): void {
          
            axios.get('http://imac-van-pieter.local:5000/activities/percentage').then(response => {
                this.data.push(response.data[0]);
                this.data.push(response.data[1]);
            });
        }
    }
    
</script>
       