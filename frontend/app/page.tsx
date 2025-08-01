"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Alert, AlertDescription } from "@/components/ui/alert"
import { Loader2, Brain, TrendingUp } from "lucide-react"
import { Slider } from "@/components/ui/slider"
import { getPrediction } from "@/src/services/api"

interface PersonalityData {
  openness: number
  conscientiousness: number
  extraversion: number
  agreeableness: number
  emotional_range: number
  conversation: number
  openness_to_change: number
  hedonism: number
  self_enhancement: number
  self_transcendence: number
}

const personalityTraits = [
  {
    key: "openness" as keyof PersonalityData,
    label: "Openness",
    description: "Openness to experience and new ideas",
  },
  {
    key: "conscientiousness" as keyof PersonalityData,
    label: "Conscientiousness",
    description: "Organization, responsibility, and dependability",
  },
  {
    key: "extraversion" as keyof PersonalityData,
    label: "Extraversion",
    description: "Sociability and assertiveness",
  },
  {
    key: "agreeableness" as keyof PersonalityData,
    label: "Agreeableness",
    description: "Cooperation and trustworthiness",
  },
  {
    key: "emotional_range" as keyof PersonalityData,
    label: "Emotional Range",
    description: "Emotional stability and resilience",
  },
  {
    key: "conversation" as keyof PersonalityData,
    label: "Conversation",
    description: "Communication and social interaction skills",
  },
  {
    key: "openness_to_change" as keyof PersonalityData,
    label: "Openness to Change",
    description: "Adaptability and flexibility",
  },
  {
    key: "hedonism" as keyof PersonalityData,
    label: "Hedonism",
    description: "Pursuit of pleasure and enjoyment",
  },
  {
    key: "self_enhancement" as keyof PersonalityData,
    label: "Self Enhancement",
    description: "Personal achievement and success",
  },
  {
    key: "self_transcendence" as keyof PersonalityData,
    label: "Self Transcendence",
    description: "Concern for others and universal values",
  },
]

export default function PersonalityPredictor() {
  const [formData, setFormData] = useState<PersonalityData>({
    openness: 50,
    conscientiousness: 50,
    extraversion: 50,
    agreeableness: 50,
    emotional_range: 50,
    conversation: 50,
    openness_to_change: 50,
    hedonism: 50,
    self_enhancement: 50,
    self_transcendence: 50,
  })

  const [isLoading, setIsLoading] = useState(false)
  const [prediction, setPrediction] = useState<any>(null)
  const [error, setError] = useState<string | null>(null)

  const handleSliderChange = (key: keyof PersonalityData, value: number[]) => {
    setFormData((prev) => ({
      ...prev,
      [key]: value[0],
    }))
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    setError(null)
    setPrediction(null)

    console.log("Form Data:", formData);

    try {
      const result = await getPrediction(formData)
      setPrediction(result)
    } catch (err) {
      setError(err instanceof Error ? err.message : "An error occurred while making the prediction")
    } finally {
      setIsLoading(false)
    }
  }

  const resetForm = () => {
    setFormData({
      openness: 50,
      conscientiousness: 50,
      extraversion: 50,
      agreeableness: 50,
      emotional_range: 50,
      conversation: 50,
      openness_to_change: 50,
      hedonism: 50,
      self_enhancement: 50,
      self_transcendence: 50,
    })
    setPrediction(null)
    setError(null)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-4xl mx-auto space-y-6">
        {/* Header */}
        <div className="text-center space-y-2">
          <div className="flex items-center justify-center gap-2">
            <Brain className="h-8 w-8 text-indigo-600" />
            <h1 className="text-3xl font-bold text-gray-900">Personality Predictor</h1>
          </div>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Analyze personality traits and get predictions based on the Big Five model and personal values. Adjust the
            sliders to reflect your personality characteristics.
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-6">
          {/* Form */}
          <Card>
            <CardHeader>
              <CardTitle>Personality Assessment</CardTitle>
              <CardDescription>
                Rate each trait on a scale from 0 to 100 based on how well it describes you.
              </CardDescription>
            </CardHeader>
            <CardContent>
              <form onSubmit={handleSubmit} className="space-y-6">
                {personalityTraits.map((trait) => (
                  <div key={trait.key} className="space-y-2">
                    <div className="flex justify-between items-center">
                      <Label htmlFor={trait.key} className="font-medium">
                        {trait.label}
                      </Label>
                      <span className="text-sm font-mono bg-gray-100 px-2 py-1 rounded">{formData[trait.key]}</span>
                    </div>
                    <p className="text-sm text-gray-600 mb-2">{trait.description}</p>
                    <Slider
                      value={[formData[trait.key]]}
                      onValueChange={(value) => handleSliderChange(trait.key, value)}
                      max={100}
                      min={0}
                      step={1}
                      className="w-full"
                    />
                  </div>
                ))}

                <div className="flex gap-2 pt-4">
                  <Button type="submit" disabled={isLoading} className="flex-1">
                    {isLoading ? (
                      <>
                        <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                        Analyzing...
                      </>
                    ) : (
                      <>
                        <TrendingUp className="mr-2 h-4 w-4" />
                        Get Prediction
                      </>
                    )}
                  </Button>
                  <Button type="button" variant="outline" onClick={resetForm}>
                    Reset
                  </Button>
                </div>
              </form>
            </CardContent>
          </Card>

          {/* Results */}
          <div className="space-y-6">
            {error && (
              <Alert variant="destructive">
                <AlertDescription>{error}</AlertDescription>
              </Alert>
            )}

            {prediction && (
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <TrendingUp className="h-5 w-5" />
                    Prediction Results
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    <div>
                      <h3 className="font-semibold text-lg">Predicted Role:</h3>
                      <p className="text-indigo-600 font-bold text-xl">
                        {prediction.predicted_role.role} ({(prediction.predicted_role.percentage).toFixed(2)}%)
                      </p>
                    </div>
                    <div>
                      <h3 className="font-semibold text-lg">Alternative Roles:</h3>
                      <ul className="list-disc list-inside space-y-1">
                        {prediction.alternative_roles.map((role: any, index: number) => (
                          <li key={index}>
                            {role.role} ({(role.percentage).toFixed(2)}%)
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                </CardContent>
              </Card>
            )}

            {/* Personality Summary */}
            <Card>
              <CardHeader>
                <CardTitle>Your Personality Profile</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-2 gap-4">
                  {personalityTraits.map((trait) => (
                    <div key={trait.key} className="space-y-1">
                      <div className="flex justify-between text-sm">
                        <span className="font-medium">{trait.label}</span>
                        <span>{formData[trait.key]}%</span>
                      </div>
                      <div className="w-full bg-gray-200 rounded-full h-2">
                        <div
                          className="bg-indigo-600 h-2 rounded-full transition-all duration-300"
                          style={{ width: `${formData[trait.key]}%` }}
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  )
}
