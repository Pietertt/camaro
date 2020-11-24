<template>
    <canvas id="pie" />
</template>

<script lang="ts">
    import { Component, Prop, Vue } from 'vue-property-decorator'
    import Chart from 'chart.js'

    @Component
    export default class Pie extends Vue {
    @Prop({ default: [] }) readonly labels!: Array<string>
    @Prop({ default: '#000000' }) readonly colors!: Array<string>
    @Prop({ default: [] }) readonly data!: Array<number>
    @Prop({default: ''}) readonly title!: string
    @Prop({
        default: () => {
            return Chart.defaults.line
        }
    })
    
    readonly options: object | undefined

    mounted() {
       this.createChart();
    }

    createChart() {
        const canvas = document.getElementById('pie') as HTMLCanvasElement

        new Chart(canvas, {
            type: 'pie',
            data: {
                labels: this.labels,
                datasets: [{ 
                    data: this.data,
                    label: this.title,
                    fill: false,
                    borderColor: this.colors,
                    backgroundColor: this.colors
                }]
            },
            options: {
                
            }
        });
    }
}
</script>