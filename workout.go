package sportmanager

import "time"

type Workout struct {
	Timestamp time.Time
	Exercises []Exercise
}
