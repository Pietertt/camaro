<template>
    <canvas id="line" />
</template>

<script lang="ts">
    import { Component, Prop, Vue } from 'vue-property-decorator'
    import Chart from 'chart.js'

    @Component
    export default class Line extends Vue {
    @Prop({ default: [] }) readonly labels!: Array<string>
    @Prop({ default: '' }) readonly color!: string
    @Prop({ default: [] }) readonly data!: Array<number>
    @Prop({ default: ''}) readonly title!: string
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
        const canvas = document.getElementById('line') as HTMLCanvasElement

        new Chart(canvas, {
            type: 'line',
            data: {
                labels: this.labels,
                datasets: [{ 
                    data: this.data,
                    label: this.title,
                    borderColor: this.color,
                    fill: false
                }]
            },
            options: {
                
            }
        });
    }
}
</script>